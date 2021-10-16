from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from universityApp.serializers.courseSerializer import CourseSerializer
from universityApp.models import Course

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Seteando permisos para cada endpoint
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
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


class CoursesByStudent(viewsets.ReadOnlyModelViewSet):

    """
    A simple ViewSet for viewing accounts.
    """
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
            
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        serializer = self.get_serializer(Course.objects.filter(students=valid_data["user_id"]), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

     

class CoursesBySemester(viewsets.GenericViewSet):

    serializer_class = CourseSerializer
    lookup_field = 'semeter_name'
    permission_classes = [AllowAny]

    def retrieve(self, request, semeter_name=None):

        queryset = Course.objects.filter(semester=semeter_name)
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


''' 
Sin usar viewSets.

class CourseCreateView(views.APIView):

    def post(self, request, *args, **kwargs):

        serializer = CourseSerializer(data=request.data) #Se crea el estudiante mediante su serializador, le pasamos la data del request.
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''
