from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    services = models.ManyToManyField(Service, blank=True)
    prices = models.IntegerField(max_length=10, blank=True, null=True)
    staff_numbers = models.IntegerField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
