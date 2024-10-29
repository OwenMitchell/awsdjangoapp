from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

app_name = 'account'

urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("create/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('profile/logout/', LogoutView.as_view(), name='logout'),
]
