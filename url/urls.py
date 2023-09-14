from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_home),
    path('<str:shortened>', views.get_shortened_url)

]
