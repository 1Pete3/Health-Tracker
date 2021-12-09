import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Lift(models.Model):
    lift_name = models.CharField(max_length=100)
    sets = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    reps = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    weight = models.DecimalField(decimal_places=2, max_digits=6,
                                 validators=[MinValueValidator(1), MaxValueValidator(1000)])
    date = models.DateField()


class Nutrition(models.Model):
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    protein = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    carbohydrates = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fat = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    date = models.DateField(default=datetime.date.today())


class Weight(models.Model):
    weight = models.DecimalField(decimal_places=1, max_digits=4,
                                 validators=[MinValueValidator(60), MaxValueValidator(1000)])
    date = models.DateField(default=datetime.date.today())
