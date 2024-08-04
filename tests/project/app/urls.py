from app import views
from django.urls import path

urlpatterns = [
    path("my_view", views.my_view),
]
