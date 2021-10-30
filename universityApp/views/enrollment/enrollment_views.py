from rest_framework import status, viewsets
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

from universityApp.serializers.enrollmentSerializer import EnrollmentSerializer
from universityApp.models import Enrollment, Course

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    # Seteando permisos para cada endpoint
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAdminUser],
                                    'retrieve': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAuthenticated],
                                    'partial_update': [IsAdminUser], }
    # Permisos

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def create(self, request):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        student_id = valid_data['user_id']
        course_id = request.data["course"]
        studentsIn = []

        course_instance = Course.objects.get(id=course_id)
        for x in course_instance.students.all():
            studentsIn.append(x.id)

        # Validamos que el estudiante no se encuentre matriculado en ese curso.
        if student_id in studentsIn:
            stringResponse = {
                'detail': 'Student is already enrolled in that course'}
            return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "student": valid_data['user_id'],
            "course": request.data['course']
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        course_instance = Course.objects.get(id=pk)
        print(course_instance.students.remove(valid_data['user_id']))

        if (course_instance.students.remove(valid_data['user_id'])):
            stringResponse = {'detail': 'Student is not logger in that course',
                              'student: ': valid_data['user_id'],
                              'course: ': pk}
            return Response(stringResponse, status=status.HTTP_200_OK)
        else:
            stringResponse = {'detail': 'Student is not enrolled in that course'}
            return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)


''' 
class EnrollmentView(views.APIView):

    def post(self, request, *args, **kwargs):

        serializer = EnrollmentSerializer(data=request.data) #Se crea el estudiante mediante su serializador, le pasamos la data del request.
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        student = request.data.pop("student")
        print(student)

        if student:
            serializer = EnrollmentSerializer(Enrollment.objects.filter(student = student), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

  
        
        serializer = EnrollmentSerializer(Enrollment.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) '''
