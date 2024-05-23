
from django.urls import path,include

from .views import UserPasswordResetView,UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendpasswordResetEmailView
urlpatterns = [
  path('login/',UserLoginView.as_view(),name="login") ,
  path('register/',UserRegistrationView.as_view(),name="register"),
  path('profile/',UserProfileView.as_view(),name="profile"),
  path('changepassword/',UserChangePasswordView.as_view(),name="changepassword"),
  path('send-reset-password-email/',SendpasswordResetEmailView.as_view(),name='send-reset-password-email'),
  path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name="reset-passwowrd"),
   
]
