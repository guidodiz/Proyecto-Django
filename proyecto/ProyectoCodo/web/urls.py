from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='web/registration/login.html'), name='login'),
	path("accounts/logout/", views.user_logout, name='logout'), 
	path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/password_reset.html"), name='password_reset'),
    path('alumnos', views.alumnos.as_view(), name='alumnos'),
    path('alta_alumno', views.alta_alumno, name='alta_alumno'),
    path('entrenador/<str:nombre>', views.entrenador, name='entrenador'),
    path('alta_entrenador', views.alta_entrenador, name='alta_entrenador'),
    path('disciplinas', views.disciplinas.as_view(), name='disciplinas'),
    path('inscripcion', views.inscripcion, name='inscripcion')
] 