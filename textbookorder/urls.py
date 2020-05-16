from django.urls import path
from . import views

# from .views import *

urlpatterns = [
    path('tbord/', views.tbord, name='tbord'),
    path('tblist/', views.tblist, name='tblist'),
]
