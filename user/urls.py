from django.urls import path
from . import views
from .views import RegisterView


urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    # path('register_user/', views.register_user, name='register'),
    path(
        'register_user/',
        RegisterView.as_view(),
        name='register'
    ),
]