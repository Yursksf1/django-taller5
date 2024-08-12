from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    
    def __str__(self):
       return "{}".format(self.name)


class Producto(models.Model):
    code = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    batch = models.CharField(max_length=100)
    manufacturing = models.DateField()
    expedition = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
       return "{}".format(self.name)