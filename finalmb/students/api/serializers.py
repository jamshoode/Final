from rest_framework import serializers
from students.models import Students, MarkAndPresence

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Students
		fields = ('first_name', 'last_name')

class MarkAndPresenceSerializer(serializers.ModelSerializer):

	class Meta:
		model = MarkAndPresence
		fields = ('marks', 'presence', 'date', 'student')


