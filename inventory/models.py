from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=95,
        verbose_name="Categoria")

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        verbose_name="Categoria del producto",
        related_name="productos",
        on_delete=models.CASCADE)

    name = models.CharField(
        max_length=95,
        verbose_name="Nombre del producto")

    image = models.CharField(
        max_length=500,
        verbose_name="Imagen de producto")

    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)
