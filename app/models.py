from django.db import models

# Create your models here.


STATE_CHOICES = (
    ("ap", "ap"),
    ("up", "up"),
    ("assam", "assam"),
    ("bihar","bihar"),
    ("karnataka","karnataka"),
    ("kerala","kerala"),
    ("tamilnadu","tamilnadu"),
    ("mp","mp"),
    ("gujarat","gujarat"),
)

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices =STATE_CHOICES ,max_length=100)


    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ("m", "mobile"),
    ('l','laptop'),
    ('tw', "topwear"),
    ('bw', "botomwear"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to="productimg")


    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ("accepted", "accepted"),
    ("packed", "packed"),
    ("on the way", "on the way"),
    ("deliverd", "deliverd"),
    ("cancel", "cancel"),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date =models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=20,default='pending')


    def __str__(self):
        return str(self.id)

