from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Alumnos', views.AlumnosViewSet, basename='alumno')
router.register(r'Entrenadores', views.EntrenadoresViewSet, basename='entrenador')

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'), name='rest_framework')
]