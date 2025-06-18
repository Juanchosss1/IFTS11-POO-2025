from django.db import models

class Edad(models.TextChoices):
    CACHORRO = 'cachorro', 'Cachorro'
    JOVEN = 'joven', 'Joven'
    ADULTO = 'adulto', 'Adulto'
    INDISTINTO = 'indistinto', 'Indistinto'
