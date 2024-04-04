from django.core.validators import MinValueValidator
from django.db import models

CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]


class Breed(models.Model):
    name = models.CharField(max_length=64)
    size_choices = [
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    ]
    size = models.CharField(max_length=10, choices=size_choices)
    friendliness = models.IntegerField(default=1, choices=CHOICES)
    trainability = models.IntegerField(default=1, choices=CHOICES)
    shedding_amount = models.IntegerField(default=1, choices=CHOICES)
    exercise_needs = models.IntegerField(default=1, choices=CHOICES)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField(MinValueValidator(limit_value=0))
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    color = models.CharField(max_length=64)
    favorite_food = models.CharField(max_length=64)
    favorite_toy = models.CharField(max_length=64)

    def __str__(self):
        return self.name
