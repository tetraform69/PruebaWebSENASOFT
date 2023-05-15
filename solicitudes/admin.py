from django.contrib import admin
from solicitudes.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Oficina)
admin.site.register(Solicitud)
admin.site.register(Respuestas)
admin.site.register(Empleado)
admin.site.register(Archivo)