from django.urls import path
from . import views

app_name = 'pdetails'

urlpatterns = [
    path('level/<int:id>', views.level, name='level'),
    path('level_sub/<int:id>', views.level, name='level_sub'),
    path('details/<int:id>/<int:lid>', views.details, name='details'),
    path('chapter-details/<int:lid>', views.chapter_details, name='sub_details'),
]
