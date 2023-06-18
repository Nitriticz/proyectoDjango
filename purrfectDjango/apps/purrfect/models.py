from django.db import models

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id, self.nombre)

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    subscribed = models.BooleanField(null=False, default=False)
    tipo = models.ForeignKey(Cargo,on_delete=models.CASCADE)

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.username, self.nombre)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id, self.nombre)
    
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "[{0}] {1}"
        return txt.format(self.id, self.nombre)

class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to="imgProductos")
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField(null=False)
    fecha_ingreso = models.DateField(auto_now_add=True)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    has_peso = models.BooleanField()

    def __str__(self):
        txt = "[{0}] {1} - {2}"
        return txt.format(self.sku,self.marca,self.nombre)
    