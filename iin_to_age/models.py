from django.db import models


# Create your models here.
class Person(models.Model):
    iin = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.iin
