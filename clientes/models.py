from django.db import models

class Cliente(models.Model):
    
    # Datos Personales del Cliente
    id_cliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Información de Contacto del Cliente
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=255)

    # Documentación y Verificación del Cliente
    identificacion = models.CharField(max_length=30, unique=True)
    licencia_conducir = models.CharField(max_length=30, unique=True)
    pais_emision_licencia = models.CharField(max_length=50)
    fecha_vencimiento_licencia = models.DateField()
    fotos_licencia = models.JSONField(default=list, blank=True)
    fotos_identificacion = models.JSONField(default=list, blank=True)

    # Información de Pago del Cliente
    metodo_pago = models.CharField(max_length=20)
    ultimos_4_digitos_tarjeta = models.CharField(max_length=4, null=True, blank=True)

    # Historial de Alquileres y Estado del Cliente
    numero_total_alquileres = models.PositiveIntegerField(default=0)
    historial_vehiculos = models.JSONField(default=list)
    historial_pagos = models.JSONField(default=list)
    historial_multas = models.JSONField(default=list)
    estado = models.CharField(max_length=30)
    notas_internas = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.id_cliente})"