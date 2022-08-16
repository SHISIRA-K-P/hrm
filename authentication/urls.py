from django.contrib import admin
from django.urls import path
from authentication.views import UserView,UserDetailView,SignInView

urlpatterns = [
    path('users/accounts',UserView.as_view()),
    path('users/accounts/<int:id>',UserDetailView.as_view()),
    path("users/accounts/login",SignInView.as_view())
]