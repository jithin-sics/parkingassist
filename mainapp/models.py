from django.db import models
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
# Create your models here.

GENDER_CHOICES = (
        ('', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
)
class Staff(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.TextField(choices=GENDER_CHOICES, null=True, blank=True)
    Phone = models.IntegerField()
    Address=models.TextField()
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
   
