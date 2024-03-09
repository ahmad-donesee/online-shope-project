from django.urls import path
from .views import register_home,login_view,logout_view

from django.utils.translation import gettext_lazy as _
app_name="register"

from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)

urlpatterns =[
    path("",register_home,name="register_home"),
    path("login/",login_view,name="login_view"),
    path("logout/",logout_view,name="logout_view"),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]