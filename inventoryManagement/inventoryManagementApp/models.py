from django.db import models

class Product(models.Model):
    barcode = models.CharField(max_length=255, unique=True, default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_images/')
    stocklevel  = models.PositiveIntegerField(default=0)
    manufacturer  = models.CharField(max_length = 255)
    categories  = models.CharField(max_length = 255)
    

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_data = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} of {self.product.title} in order {self.order.id}'

    def get_total_price(self):
        return self.quantity * self.price
