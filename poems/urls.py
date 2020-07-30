from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path(name="poet"),
    # path(name="poem"),
]
