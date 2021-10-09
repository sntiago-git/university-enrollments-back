from django.db import models
from .course import Course
from .student import Student


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    student = models.ForeignKey(
        Student, related_name="enrollment", on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, related_name="enrollment", on_delete=models.CASCADE)
