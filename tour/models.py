from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Horse(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='horse')

    def __str__(self):
        return f"{self.name} - {self.owner}"
    

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name
    

class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reviews')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews')
    
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES)
    text = models.TextField()

    def __str__(self):
        return f"{self.person} -> {self.company} ({self.rating})"
    

# Create your models here.
