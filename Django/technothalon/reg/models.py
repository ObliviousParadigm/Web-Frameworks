from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class team(models.Model):
	name = models.CharField(max_length=25)
	CATEGORY_CHOICES = (
		('Zeus University', 'Zeus University'),
		('Apollo University', 'Apollo University'),
		('Nike University', 'Nike University'),
		('Hermes University', 'Hermes University'),
	)
	uni = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
	number_of_members = models.IntegerField(
		default=5,
		validators=[MaxValueValidator(25),
					MinValueValidator(5)
					]
	)
	boarding = models.BooleanField()

	def __str__(self):
		return self.name
