from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    sno = models.PositiveSmallIntegerField()
    name = models.TextField()
    srn = models.CharField(max_length=15)
    att = models.BooleanField()

    def give_att(self):
        return self.att
    
    def __str__(self):
        return self.name