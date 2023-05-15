from django.db import models
from django.contrib.auth.models import AbstractUser

solicitudEstado = [
    ('Solicitada', 'Solicitada'),
    ('Atendida', 'Atendida')
]

solicitudTipo = [
    ('Peticion', 'Peticion'),
    ('Queja', 'Queja'),
    ('Reclamo', 'Reclamo')
]
# Create your models here.


class User(AbstractUser):

    def __str__(self) -> str:
        return f"{self.username} - {self.groups}"


class Oficina(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nombre


class Empleado(models.Model):
    identificacion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(max_length=45)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    oficina = models.ForeignKey(Oficina, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.oficina.nombre}"


class Solicitud(models.Model):
    codigo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=2000)
    correo = models.EmailField(max_length=45)
    barrio = models.CharField(max_length=45)
    estado = models.CharField(choices=solicitudEstado, max_length=45)
    tipo = models.CharField(choices=solicitudTipo, max_length=45)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.codigo} - {self.oficina.nombre}"


class Respuestas(models.Model):
    respuesta = models.CharField(max_length=2000)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"Respuesta: {self.solicitud.codigo} - {self.solicitud.oficina.nombre}"

class Archivo(models.Model):
    archivo = models.FileField(upload_to="resources/", null=True, blank=True)
    solicitud = models.ForeignKey(Solicitud, null=True, blank=True, on_delete=models.PROTECT)
    respuesta = models.ForeignKey(Respuestas, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.solicitud or self.respuesta