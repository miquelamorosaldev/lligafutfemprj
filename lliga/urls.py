from django.urls import path

from . import views, api

# app_name = "lliga"
urlpatterns = [
    # ex: /lliga/
    path("", views.index, name="index"),
    # ex: /lliga/1/
    path("<int:lliga_id>/", views.detail, name="detail"),
    # ex: /lliga/equips/1/
    path("equip_detail/<int:equip_id>/", views.equip_detail, name="equip_detail"),
    path('get_lligues', api.get_lligues ),
    path('get_equips/<int:lliga_id>', api.get_equips ),
]