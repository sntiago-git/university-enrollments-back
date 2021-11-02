from universityApp.models.course import Course
from ..models.course import Course
from rest_framework import serializers
from universityApp.serializers.teacherSerializer import TeacherRelatedField


class CourseSerializer(serializers.ModelSerializer):

    '''
     Usamos el nuevo serializador para obtener los datos del profesor
     que serán mostrados en el curso. (Name y lastname)
    '''
    teacher = TeacherRelatedField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
