from django.urls import path
from .views import students

urlpatterns = [
    path('', students, name='students'),
]