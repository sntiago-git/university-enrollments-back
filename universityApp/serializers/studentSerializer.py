from rest_framework import serializers
from universityApp.models.student import Student
from universityApp.models.career import Career


class StudentSerializer(serializers.ModelSerializer):

    career = serializers.CharField()

    class Meta:
        model = Student
        fields = ['id', 'password', 'name', 'lastname',
                  'birthdate', 'gender', 'phone', 'email', 'career']


    '''
    Ya que nuestro modelo estudiante
    tiene una llave foranea (career)
    se debe sobreescribir el metodo create. 
    '''

    def create(self, validated_data):

        #Se extrae el valor de career (carrera del estudiante) enviado desde el request.
        career = validated_data.pop('career') 
        
        #Se crea o se obtiene el objeto career.
        career_instance, created = Career.objects.get_or_create(name=career) 
        
        if(created):
            print("La Carrera:", career_instance.__str__(), "ha sido creada en Base de datos.")

        #Se crea el nuevo objeto estudiante junto a su objeto career
        student_instance = Student.objects.create(**validated_data, career=career_instance)

        print("El Estudiante:", student_instance.__str__(), "ha sido creado en Base de datos.")

        return student_instance
   
    ''' 
    def to_representation(self, obj):

        student = Student.objects.get(id=obj.id)
        career = Career.objects.get(id=obj.career)

        return {
            'id': student.id,
            'name': student.name,
            'lastname': student.lastname,
            'birthdate': student.birthdate,
            'gender': student.gender,
            'phone': student.phone,
            'email': student.email,
            'career': {
                'id': career.id,
                'name': career.name,
            }
        }
    '''