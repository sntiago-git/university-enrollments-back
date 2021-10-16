"""universityProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

# Swagger API
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from universityApp import views



#Swagger Interface
schema_view = get_schema_view(
    openapi.Info(
        title="Endpoints University Project",
        default_version='v1',
        description="Documentación de Endpoints, Proyecto Universidad - Gestion de matriculas. P36 - Grupo 3",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sntiagomeneses@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    #path('student/', views.studentView.StudentCreateView.as_view()),
    #path('student/<int:pk>/', views.studentView.StudentCreateView.as_view()),

    path('teacher/', views.teacherView.TeacherCreateView.as_view()),
    path('enrollment/', views.enrollmentView.EnrollmentView.as_view()),
    

    path('students/', include('universityApp.views.student.router')),
    path('courses/', include('universityApp.views.course.router')),

    #Swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


