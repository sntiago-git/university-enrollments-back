from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from universityApp.serializers.studentSerializer import StudentSerializer
from universityApp.models import Student

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    # Seteando permisos para cada endpoint
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [IsAdminUser],
                                    'retrieve': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'partial_update': [IsAdminUser], }
    # Permisos

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):

        # Se crea el estudiante mediante su serializador, le pasamos la data del request.

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"id": request.data["id"],
                     "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class StudentsByCourse(viewsets.GenericViewSet):

    serializer_class = StudentSerializer
    lookup_field = 'course_id'
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, course_id=None):

        queryset = Student.objects.filter(course=course_id)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetMyInfo(viewsets.GenericViewSet):

    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        # Respondemos los datos del estudiante autenticado.
        data = self.get_serializer(Student.objects.filter(
            id=valid_data['user_id']))
        return Response(data.data, status=status.HTTP_200_OK)
