from django.db import models

# Create your models here.

DEFAULT_LENGTH = 255

class Product(models.Model):
    name = models.CharField(max_length=DEFAULT_LENGTH) # Nombre del producto
    price = models.IntegerField(default=0) # Precio del producto
    url = models.URLField() # URL del producto
    created_at = models.DateTimeField(auto_now_add=True) # Fecha de creación del producto
    updated_at = models.DateTimeField(auto_now=True) # Fecha de actualización del producto

    # El metodo __str__ representa el objeto como cadena de caracteres
    def __str__ (self): 
        return f"{self.name} - {self.price}"