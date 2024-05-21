from django.contrib import admin
from .models import Chofer,RegistroContabilidad,Vehiculo

# Register your models here.
admin.site.register(Chofer)
admin.site.register(RegistroContabilidad)
admin.site.register(Vehiculo)