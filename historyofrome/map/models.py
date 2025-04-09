from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = []  # Remove username from required fields
    
class Event(models.Model):
    """used for tracking a single discrete event"""
    summary = models.CharField(blank=True, null=True, max_length=50)
    details = models.TextField(null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=50)

class PointEvent(Event):
    location = models.PointField()

class PolyEvent(Event):
    bbox = models.PolygonField()

# class BaseMap(models.Model)
# class Boundary(models.Model)