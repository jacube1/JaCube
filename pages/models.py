from django.db import models

# Create your models here.


class Cart(models.Model):
    owner = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    products_counter = models.CharField(max_length=100)

    def __str__(self):
        return self.owner


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name, self.cart.owner
