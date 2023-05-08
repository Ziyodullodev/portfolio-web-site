from django.urls import path
from .views import homeview

urlpatterns = [
    path('', homeview, name="home")
]