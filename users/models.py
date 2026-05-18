from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/')
    resume = models.FileField(upload_to='resumes/')
    phone_number = models.CharField(max_length=15, default="+996")
    GENDER = (
        ('М', 'М'),
        ('Ж', 'Ж')
    )
    gender = models.CharField(choices=GENDER, max_length=2)
    address = models.CharField(max_length=100)
    experience = models.TextField()
    education = models.CharField(max_length=200)
    skills = models.TextField()


    def __str__(self):
        return super().__str__()

# Create your models here.
