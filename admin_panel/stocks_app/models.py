from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.TextField()

class Position(models.Model):
    name = models.TextField()

class Priority(models.Model):
    number = models.IntegerField()

class Country(models.Model):
    name = models.IntegerField()

class Type(models.Model):
    name = models.TextField()

class Item(models.Model):
    name = models.TextField()
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True)
    stock = models.ForeignKey("Stock", on_delete=models.SET_NULL, null=True)
    arrival_time = models.TimeField()
    arrival_date = models.DateField()
    point_of_departure = models.ForeignKey("Place", on_delete=models.SET_NULL, null=True)

class Stock(models.Model):
    name = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null=True)

class Emploee(models.Model):
    name = models.TextField()
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey("Priority", on_delete=models.SET_NULL, null=True)
    birth_year = models.DateField()

class Emploee_Stock(models.Model):
    stock_id = models.ForeignKey("Stock", on_delete=models.SET_NULL, null=True)
    emploee_id = models.ForeignKey("Emploee", on_delete=models.SET_NULL, null=True)

class Place(models.Model):
    name = models.TextField()
    organization = models.ForeignKey("Organization", on_delete=models.SET_NULL, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null=True)
