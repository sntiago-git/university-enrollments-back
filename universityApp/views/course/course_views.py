from rest_framework import status, views, viewsets
from rest_framework import response
from rest_framework.response import Response


from universityApp.serializers.courseSerializer import CourseSerializer
from universityApp.serializers.studentSerializer import StudentSerializer
from universityApp.models.course import Course


class CourseViewSet(viewsets.ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
        

class CoursesByStudent(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):

        queryset = Course.objects.filter(students = 2)
        print(queryset)
        serializer =  CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CoursesBySemester(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):

        queryset = Course.objects.filter(students = 2)
        print(queryset)
        serializer =  CourseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


''' 
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