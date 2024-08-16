from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(unique=True, max_length=100, null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)


class Producto(models.Model):
    code = models.CharField(unique=True, max_length=50, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    batch = models.CharField(max_length=100, null=True, blank=True)
    manufacturing = models.DateField(null=True, blank=True)
    expedition = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return "{}".format(self.name)