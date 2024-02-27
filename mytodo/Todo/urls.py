from django.contrib import admin
from django.urls import path

from .import views
from .import *

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.sign_up,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('add-todo',views.add_todo,name="add-todo"),
    path('delete_todo/<int:id>',views.delete_todo,name="delete_todo"),
    path("change-status/<int:id>/<str:status>",views.change_todo,name="change-status")
]
