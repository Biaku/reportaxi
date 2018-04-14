from django.contrib.auth.models import User
from django.db import models


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class Taxi(CommonInfo):
    CALIFICACION = (
        (1, 'Malo'),
        (2, 'Regular'),
        (3, 'Bueno'),
    )
    COLOR = (
        (1, 'Amarillo'),
        (2, 'Blanco')
    )
    numero = models.PositiveSmallIntegerField()
    calificacion = models.PositiveSmallIntegerField(choices=CALIFICACION, default=2)
    comentario = models.TextField(max_length=255)
    color = models.PositiveSmallIntegerField(choices=COLOR, default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taxis')
    costo = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.numero) + " " + str(self.calificacion) + " " + self.usuario.username

    class Meta:
        db_table = 'taxi'
