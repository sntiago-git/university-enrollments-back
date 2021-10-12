from django.db import models
from .course import Course
from .student import Student


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    date_joined = models.DateField("Date_joined")
    