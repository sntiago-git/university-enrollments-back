from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..serializers.studentSerializer import StudentSerializer
from ..models.student import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings


class StudentCreateView(generics.RetrieveAPIView):

    def post(self, request, *args, **kwargs):

        # Se crea el estudiante mediante su serializador, le pasamos la data del request.
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"id": request.data["id"],
                     "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = (IsAuthenticated,)
        
    def get(self, request, *args, **kwargs):

    
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        ''' 
        if valid_data['id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)'''

        return super().get(request, *args, **kwargs)
