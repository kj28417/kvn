from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    completada = models.DateTimeField(null=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + " - por: " + self.usuario.username 
    