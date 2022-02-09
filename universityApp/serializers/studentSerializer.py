from django.db.models.query_utils import Q
from rest_framework import serializers
from universityApp.models.student import Student
from universityApp.models.career import Career

from django.core import exceptions
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators


class StudentSerializer(serializers.ModelSerializer):

    career = serializers.CharField()
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'password', 'password2', 'name', 'lastname',
                  'birthdate', 'gender', 'phone', 'email', 'career']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    '''
    Ya que nuestro modelo estudiante
    tiene una llave foranea (career)
    se debe sobreescribir el metodo create.
    '''

    def create(self, validated_data):

        # Se extrae el valor de career (carrera del estudiante) enviado desde el request.
        career = validated_data.pop('career')

        # Validamos que las contraseñas coincidan.
        password = validated_data["password"]
        password2 = validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords must match"})
        validated_data.pop('password2')

        validated_data["password"] = self.verify_password(
            password)  # Validamos y encriptamos la password

        # Se crea o se obtiene el objeto career.
        career_instance, created = Career.objects.get_or_create(name=career)

        # Se crea el nuevo objeto estudiante junto a su objeto career
        print(validated_data)
        student_instance = Student.objects.create(
            **validated_data, career=career_instance)

        return student_instance

    def verify_password(self, password):

        errors = dict()

        try:
            # validate the password and catch the exception
            validators.validate_password(password=password)

            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            password = make_password(password, some_salt)  # Encrypt
            print(password)
            return password

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)

    def update(self, instance, validated_data):

        # no modificable !NO SIRVE, CREAR OTRO SERIALIZADOR PERSONALIZADO PARA EL UPDATE DEL MODELO.

        career = validated_data.get('career')

        ''' 
        id = validated_data.get('id')
        password = validated_data.get('password')

        

        if(id):
            raise serializers.ValidationError(
                {"id": "id cannot be modified"}
            )

        if(password):
            raise serializers.ValidationError(
                {"password": "password cannot be modified"}
            )
       '''

        if (career):
            print(career)
            # Se crea o se obtiene el objeto career.
            career_instance, created = Career.objects.get_or_create(
                name=career)
            validated_data['career'] = career_instance
       
        return super().update(instance, validated_data)
