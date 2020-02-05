from django.urls import path

from . import views

urlpatterns = [
     path('hisse/<str:name>/', views.hisse),
]