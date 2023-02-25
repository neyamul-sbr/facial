from django.db import models
from django.db.models.query import QuerySet
import numpy as np



# Create your models here.
class CapTable(models.Model):
    name = models.CharField(max_length= 50, null= True)
    age = models.CharField(max_length= 10, null= True)


