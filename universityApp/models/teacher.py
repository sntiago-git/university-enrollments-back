from django.db import models


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField('Name', max_length=45)
    lastname = models.CharField('Lastname', max_length=45)
    birthdate = models.DateField('Birthdate')
    gender = models.CharField("Gender", max_length=15)
    phone = models.CharField("Phone", max_length=15)
    email = models.EmailField('Email', max_length=100)
    