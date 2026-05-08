from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    # services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
