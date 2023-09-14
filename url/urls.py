from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_home),
    path('<str:url>', views.get_shortened_url)

]
