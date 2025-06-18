from django.db import models

class EstadoSalud(models.TextChoices):
    SALUDABLE = 'saludable', 'Saludable'
    HERIDO = 'herido', 'Herido'
    ENFERMO = 'enfermo', 'Enfermo'
    ENLASULTIMAS = 'enlasultimas', 'En las últimas'
    RECUPERADO = 'recuperado', 'Recuperado'