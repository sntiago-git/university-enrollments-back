from django.db.models.query import QuerySet
from rest_framework import status, views, viewsets
from rest_framework.response import Response

from universityApp.serializers.courseSerializer import CourseSerializer
from universityApp.models.course import Course


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class CoursesByStudent(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Course.objects.filter(students = 2)
    serializer_class = CourseSerializer

    
class CoursesBySemester(viewsets.GenericViewSet):

    serializer_class = CourseSerializer
    lookup_field = 'semeter_name'

    def retrieve(self, request, semeter_name = None):

        queryset = Course.objects.filter(semester = semeter_name)
        serializer =  CourseSerializer(queryset, many=True)
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