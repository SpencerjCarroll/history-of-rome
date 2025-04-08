from django.db import models

# Create your models here.

class PointEvent(models.Model):
    """used for tracking a single discrete event"""
    summary = models.CharField()
    details = models.TextField()
    location = models.PointField()
    date = models.DateField()

class RangeEvent(models.Model):
    """used for tracking extented events"""
    summary = models.CharField()
    details = models.TextField()
    location = models.PolygonField()
    start_date = models.DateField()
    end_date = models.DateField()

# class BaseMap(models.Model)
# class Boundary(models.Model)