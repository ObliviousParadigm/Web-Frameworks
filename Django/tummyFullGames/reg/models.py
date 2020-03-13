from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class tribute(models.Model):
    name = models.CharField(max_length=25)
    skill = models.CharField(max_length=15)
    district = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(4),
                    MinValueValidator(1)
                    ]
    )
    text = models.TextField()
    # track = models.SmallIntegerField()

    def __str__(self):
        return self.name
