from django.urls import path
from . import views

urlpatterns = [
    path('<str:url>', views.get_shortened_url)
]
