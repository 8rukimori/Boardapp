from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signupfunc, name="signup"),
    path("login/", views.loginfunc, name="login"),
    path("", views.listfunc, name="list"),
    path("logout/", views.logout_view, name="logout"),
    path("detail/<int:pk>", views.detailfunc, name="detail"),
    path("like/<int:pk>", views.likefunc, name="like"),
    path("read/<int:pk>", views.readfunc, name="read"),
    path("create/", views.BoardCreate.as_view(), name="create"),
]
