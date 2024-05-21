
from django.urls import path,include

from .views import UserRegistrationView,UserLoginView
urlpatterns = [
  path('login/',UserLoginView.as_view(),name="login") ,
path('register/',UserRegistrationView.as_view(),name="register"),

   
]
