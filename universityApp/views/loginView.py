
#Sobrescribiendo el response del login para que devuelva los tokens y ademas el nombre y id del user.

# Import external packages
from rest_framework_simplejwt.views import TokenObtainPairView as SimpleTokenObtainPairView

# Import my packages
from universityApp.serializers.loginSerializer import MyTokenObtainPairSerializer


class TokenObtainPairView(SimpleTokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer