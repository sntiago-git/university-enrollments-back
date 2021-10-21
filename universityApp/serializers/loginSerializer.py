from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#Sobreescribimos el serializador del login para poder devolver mas datos ademas de los tokens

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        return {
            "id": self.user.id,
            "name": self.user.name,
            "lastname": self.user.lastname,
            **attrs,
        }
