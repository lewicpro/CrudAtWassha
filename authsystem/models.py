from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
import random, string

# Create your models here.

class authdataModel(models.Model):
    user= models.OneToOneField(User, null=True)
    datavalue = models.CharField(max_length=1, blank=True, default=0)


class NamesModel(models.Model):
    user= models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    year = models.CharField(max_length=120, blank=True, null=True)
