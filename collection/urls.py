from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_home_page_data, name='home'),
    path(
        'user-<str:username>/',
        views.get_personal_page_data,
        name='personal_page'
    ),
    path(
        'user-<str:username>/create-collection',
        views.create_collection,
        name='create_collection'
    ),
]