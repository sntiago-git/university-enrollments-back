from django.db import models

class Career(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField("Name", max_length=15)
    