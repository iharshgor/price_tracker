from django.urls import path

from . import views

app_name = "tracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.detail, name="detail"),
]
