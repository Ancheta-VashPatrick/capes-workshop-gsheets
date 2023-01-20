from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.signin, name='login'), # URL for logging in
    path('logout/', views.signout, name='logout'), # URL for logging out 
    # path('register/', views.register, name='register'), # URL for registering (function-based)
    path('register/', views.RegistrationView.as_view(), name='register'), # URL for registering (class-based)
]