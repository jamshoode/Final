from django.db import models

class Students(models.Model):
	first_name = models.TextField()
	last_name = models.TextField()

class MarkAndPresence(models.Model):
	marks = models.IntegerField()
	presence = models.BooleanField()
	date = models.DateField()
	student = models.ForeignKey(Students,
	on_delete=models.CASCADE)

