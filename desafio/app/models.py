from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    #creacion_registro = models.DateField(auto_now_add=True) -> agrega un registro de cuando se creo el elemento
        
    def __str__(self):
        return f"{self.marca}/{self.modelo}/{self.patente}"
    
class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo_id = models.OneToOneField("Vehiculo", related_name='Chofer',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.rut} {self.nombre} {self.apellido}"
    
class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    vehiculo_id = models.OneToOneField("Vehiculo", related_name='contabilidad',on_delete=models.PROTECT)
    creacion_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.valor} / {self.vehiculo_id} / {self.creacion_registro}"
    


