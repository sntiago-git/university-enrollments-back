from django.db import models
from .teacher import Teacher


class Course(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField("Name", max_length=15)
    short_desc = models.TextField("Short_desc", max_length=45)
    long_desc = models.TextField("Long_desc", max_length=300)
    schedule = models.TextField("Schedule", max_length=300)
    semester = models.CharField("Semester", max_length=20)
    credits = models.IntegerField("Credits")
    teacher = models.ForeignKey(
        Teacher, related_name="course", on_delete=models.CASCADE)
