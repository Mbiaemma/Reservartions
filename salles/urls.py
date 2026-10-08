"""Tache 3 : brancher les ViewSets sur un DefaultRouter.

Les routes attendues sont (prefixe /api/ deja fourni par config/urls.py) :
  /api/salles/            /api/salles/{id}/
  /api/reservations/      /api/reservations/{id}/
  /api/salles/{id}/occupation/
"""
from django.urls import path, include
from rest_framework import routers

from .views import SalleViewSet, ReservationViewSet

router = routers.DefaultRouter()

router.register(r'salles', SalleViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
