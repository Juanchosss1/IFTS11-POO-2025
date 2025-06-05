from django.db import models

class RazaPerro(models.TextChoices):
    LABRADOR = 'labrador', 'Labrador'
    CANICHE = 'caniche', 'Caniche'
    BULLDOG = 'bulldog', 'Bulldog'
    OVEJERO = 'ovejero', 'Ovejero'
    OTRO = 'otro', 'Otro'