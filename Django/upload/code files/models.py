from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Movie(models.Model):
	name=models.CharField(max_length=200)
	year=models.PositiveIntegerField()
	cast=models.TextField()
	def __str__(self):
		return self.name