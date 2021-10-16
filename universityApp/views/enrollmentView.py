from rest_framework import serializers, status, views, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..serializers.enrollmentSerializer import EnrollmentSerializer
from ..models.enrollment import Enrollment

''' 
class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
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
        return Response(serializer.data, status=status.HTTP_200_OK) 