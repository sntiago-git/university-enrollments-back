from ..models.teacher import Teacher
from rest_framework import serializers


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name + " " + value.lastname

    ''' Creamos un serializador related field para devolver ciertos 
    datos cuando se haga el llamado desde otra tabla.'''
