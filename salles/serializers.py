"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Reservation, Salle

from .permissions import IsOwnerOrReadOnly

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ['nom', 'capacite', 'batiment']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('salle', 'utilisateur', 'debut', 'fin', 'motif', 'statut', 'cree_le')
        read_only_fields = ['utilisateur']
        permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def validate(self, data):
        if data['debut'] > data['fin']:
            raise serializers.ValidationError(
                "La date de fin de la reservation n’est pas strictement postérieure à celle de début"
            )
        return data

