from app import views
from django.urls import path

urlpatterns = [
    path("echo", views.echo),
    path("decorated_echo", views.decorated_echo),
]
