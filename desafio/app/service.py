from .models import Chofer, Vehiculo, RegistroContabilidad


def crear_vehiculo(patente,marca,modelo,year,activo):
    vehiculo = Vehiculo(
        patente = patente,
        marca=marca,
        modelo= modelo,
        year=year,
        activo=activo
    )
    vehiculo.full_clean()
    vehiculo.save()
    return vehiculo

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return vehiculo

def crear_chofer(rut,nombre,apellido,activo,vehiculo_id):
    vehiculo = obtener_vehiculo(vehiculo_id)
    chofer = Chofer(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        vehiculo_id=vehiculo
        )
    chofer.save()
    return chofer

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra,valor, vehiculo_id,creacion_registro):
    vehiculo = obtener_vehiculo(vehiculo_id)
    registro = RegistroContabilidad(
        fecha_compra=fecha_compra,
        valor=valor,
        vehiculo_id=vehiculo,
        creacion_registro=creacion_registro
    )
    registro.save()
    return registro
    
def deshabilitar_chofer(chofer):
    chofer.activo = False
    chofer.save()
    return chofer 

def habilitar_chofer(chofer):
    chofer.activo = True
    chofer.save()
    return chofer

def deshabilitar_vehiculo(vehiculo):
    vehiculo.activo = False
    vehiculo.save()
    return vehiculo

def habilitar_vehiculo(vehiculo):
    vehiculo.activo = True
    vehiculo.save()
    return vehiculo

def imprimir_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for v in vehiculos:
        print (f"""Vehiculo: {v.patente}/{v.marca}/{v.modelo}/{v.year}/activo:{v.activo}""")

        if hasattr(v, 'chofer'):
            print(f""" Chofer[{v.chofer.rut}]: {v.chofer.nombre}{v.chofer.apellido}/activo:{v.chofer.activo}""")

        if hasattr(v, 'contabilidad'):
            print(f"""Contabilidad:[{v.contabilidad.id}]: Fecha compra: {v.contabilidad.fecha_compra}/ valor:{v.contabilidad.valor}  """)

