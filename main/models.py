from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    about = models.TextField()
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(default=0)


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-posters/")
    product = models.ForeignKey(Products,  on_delete=models.CASCADE, related_name="images")


class ProductSize(models.Model):
    size = models.CharField(max_length=250)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE, related_name="sizes")


class ProductColor(models.Model):
    color = models.CharField(max_length=250)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE, related_name="colors")


class ProductReviews(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    review = models.TextField()
    star = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE, related_name="reviews")


class Orders(models.Model):
   user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="orders")
   date_added = models.DateTimeField(auto_now_add=True)
   adderess = models.TextField()
   phone_number = models.CharField(max_length=13)
            

class OrderItems(models.Model):
    quanitity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Products,  on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="items")
