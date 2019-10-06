from django.urls import path
from .views import home, DetailView 
urlpatterns = [
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('', home, name='home'),
]