
from django.urls import path
from quiz import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('register',views.registerPage, name="register"),
    path('addQuestion',views.addQuestion,name="addQuestion"),
    path('logout', views.logoutUser, name="logout")
]
