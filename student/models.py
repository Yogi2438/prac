from django.db import models

class student(models.Model):
	name=models.CharField(max_length=25)
	std=models.CharField(max_length=25)
	roll_no=models.IntegerField()
	password=models.CharField(max_length=10)

	def __str__(self):
		return self.name