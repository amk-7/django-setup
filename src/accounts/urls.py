
from django.urls import path

from . import views


app_name = "accounts"

urlpatterns = [
    path('login', view=views.login_user, name='login'),
    path('logout', view=views.logout_user, name='logout'),
    path('forget_password', view=views.forget_password, name='forget_password'),
    path('reset_password', view=views.reset_password, name='reset_password'),
]
