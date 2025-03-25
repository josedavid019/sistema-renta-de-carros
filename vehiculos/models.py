from django.db import models

class Vehiculo(models.Model):

    # Datos básicos del vehículo
    id_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    tipo = models.CharField(max_length=30)
    numero_puertas = models.PositiveIntegerField()
    capacidad_pasajeros = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    fecha_incorporacion = models.DateField(auto_now_add=True)

    # Especificaciones técnicas del vehículo
    tipo_combustible = models.CharField(max_length=20)
    transmision = models.CharField(max_length=20)
    kilometraje = models.PositiveIntegerField()
    potencia_motor = models.DecimalField(max_digits=6, decimal_places=2)
    consumo_combustible = models.DecimalField(max_digits=4, decimal_places=2)
    capacidad_maletero = models.PositiveIntegerField()

    # Información de renta del vehículo
    precio_alquiler_dia = models.DecimalField(max_digits=10, decimal_places=2)
    deposito_seguridad = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=100)
    fecha_ultima_renta = models.DateField(null=True, blank=True)

    # Documentación y mantenimiento del vehículo
    placa = models.CharField(max_length=10, unique=True)
    vin = models.CharField(max_length=20, unique=True)
    seguro_vigente = models.BooleanField(default=True)
    fecha_vencimiento_seguro = models.DateField(null=True, blank=True)
    estado_documentacion = models.CharField(max_length=100)
    historial_mantenimientos = models.TextField(blank=True)
    ultima_inspeccion = models.DateField(null=True, blank=True)
    fecha_ultimo_mantenimiento = models.DateField(null=True, blank=True)
    proximo_mantenimiento = models.DateField(null=True, blank=True)

    # Historial y valoración del vehículo
    historial_accidentes = models.TextField(blank=True)
    valor_actual = models.DecimalField(max_digits=12, decimal_places=2)

    # Imágenes y detalles adicionales del vehículo
    fotos = models.JSONField(default=list, blank=True)
    descripcion_adicional = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
