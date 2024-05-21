from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('profile/<str:name>', views.profile, name='profile'),
    path('books', views.books, name='books'),
    path('rent', views.rent, name='rent'),
]