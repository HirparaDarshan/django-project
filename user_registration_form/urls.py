from django.urls import path
from user_registration_form.views import home, login_view, register_view, logout_view

urlpatterns = [
    # When user visits "" (homepage)
    path("", home, name="home"),
    # /register/ URL
    path("register/", register_view, name="register"),
    # /login/ URL
    path("login/", login_view, name="login"),
    # /logout/ URL
    path("logout/", logout_view, name="logout"),
]
