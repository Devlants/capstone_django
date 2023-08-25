from django.db import models

# Create your models here.
class Signal(models.Model):
    staus = models.BooleanField(default = False)
