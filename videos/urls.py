from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
    path('<int:video_id>/', views.watch_video, name='watch_video'),
]