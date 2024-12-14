from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.course_list, name='course_list'),
    path('progress/<int:course_id>/', views.track_progress, name='track_progress'),
]
