from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from .models import Students, MarkAndPresence
from students.api.serializers import StudentSerializer, MarkAndPresenceSerializer
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

class StudentListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'date']

class Map(APIView):

	def getAll(self, request, format=None):
		queryset = MarkAndPresence.objects.all()
		serializer = MarkAndPresenceSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = MarkAndPresenceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def get_object(self, pk):
		try:
			return MarkAndPresence.objects.get(pk=pk)
		except Student.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		student = self.get_object(pk)
		serializer = MarkAndPresenceSerializer(student)
		return Response(serializer.data)	