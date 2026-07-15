from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18,message="You must be at least 18 years old."),
            MaxValueValidator(120,message="Please enter a valid age.")
            ]
            )
    email = models.EmailField()

    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
