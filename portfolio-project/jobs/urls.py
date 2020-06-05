from django.urls import path ,include
from .import views

urlpatterns = [
    path('' , views.home.as_view() , name='home')
]
