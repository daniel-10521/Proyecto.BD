from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Relación con el usuario

    def __str__(self):
        return self.title + ' - by ' + self.user.username
    
    from django.db import models

# 1. Modelo para tus Datos Personales
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100, help_text="Ej: Estudiante de TI")
    ubicacion = models.CharField(max_length=100, default="Manta, Ecuador")
    cedula = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50, default="Ecuatoriana")
    nacimiento = models.CharField(max_length=50, help_text="Ej: 2005 (21 años)")
    celular = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20, default="Soltero")
    email = models.EmailField()
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True) # Necesitas configurar media

    def __str__(self):
        return self.nombre

# 2. Modelo para Experiencia Laboral
class Experiencia(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

# 3. Modelo para Cursos/Educación
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default="Completado")

    def __str__(self):
        return self.titulo