from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..serializers.courseSerializer import CourseSerializer


class CourseCreateView(views.APIView):

    def post(self, request, *args, **kwargs):

        serializer = CourseSerializer(data=request.data) #Se crea el estudiante mediante su serializador, le pasamos la data del request.
        serializer.is_valid(raise_exception=True)
        serializer.save()

        ''' 
        tokenData = {"id": request.data["id"],
                     "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True) '''

        return Response(status=status.HTTP_201_CREATED)
