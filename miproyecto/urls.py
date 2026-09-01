"""Direcciones web de ReservaGol."""

from django.urls import path

from core.views import resumen


urlpatterns = [
    path("", resumen, name="inicio"),
    path("reservas/", resumen, name="resumen"),
]
