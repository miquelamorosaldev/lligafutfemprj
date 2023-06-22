from django.urls import path

from . import views

# app_name = "lliga"
urlpatterns = [
    # ex: /lliga/
    path("", views.index, name="index"),
    # ex: /lliga/1/
    path("<int:lliga_id>/", views.detail, name="detail"),
]