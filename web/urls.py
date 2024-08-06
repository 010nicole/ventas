
from django.urls import path
from . import views 
urlpatterns = [
    path('about/', views.acerca),
    path('',views.home)
]