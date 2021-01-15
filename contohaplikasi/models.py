from django.db import models

# Create your models here.
class StaffIT(models.Model):
    nama = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=8)
    angkatan = models.IntegerField()

