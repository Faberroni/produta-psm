from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path("form/", contactView, name="contact_form"),
    path("success/", successView, name="success"),
]