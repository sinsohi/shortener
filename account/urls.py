from django.urls import path
from . import views
app_name = "account"
urlpatterns = [
    path('register',views.show_register,name= 'register'),
    path('login',views.show_login,name='login')

]
