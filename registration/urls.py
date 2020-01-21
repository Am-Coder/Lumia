from django.urls import path, re_path
from . import views

app_name = 'register'

urlpatterns = [
    re_path(r"^$", views.enter, name="index"),
    re_path(r"^signin/$", views.signin, name="signin"),
    re_path(r"^signup/$", views.signup, name="signup")
]
