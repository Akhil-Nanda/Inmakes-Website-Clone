from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('internship/', views.internship, name='internship'),
]
