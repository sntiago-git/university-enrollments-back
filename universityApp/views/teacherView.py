from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..serializers.teacherSerializer import TeacherSerializer
from universityApp.models import Teacher


class TeacherCreateView(views.APIView):

    def post(self, request, *args, **kwargs):

        serializer = TeacherSerializer(data=request.data) #Se crea el Profesor mediante su serializador, le pasamos la data del request.
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
        
    def get(self, request):

        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
