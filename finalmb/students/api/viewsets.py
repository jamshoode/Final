from students.models import Students, MarkAndPresence
from .serializers import StudentSerializer, MarkAndPresenceSerializer
from rest_framework import viewsets
from rest_framework import generics

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Students.objects.all()
	serializer_class = StudentSerializer

class StudentMarkPresenceViewSet(viewsets.ModelViewSet):
	queryset = MarkAndPresence.objects.all()
	serializer_class = MarkAndPresenceSerializer