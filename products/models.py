# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.PositiveIntegerField()
#     brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)
#     categories = models.ManyToManyField('ProductCategory')
#     discount = models.PositiveSmallIntegerField(null=True, blank=True)
#     stock = models.PositiveIntegerField()

# class ProductAppearance(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/%Y/%m/%d/')
#     color = models.CharField(max_length=25)

# class Brand(models.Model):
#     name = models.CharField(max_length=50)
#     logo = models.ImageField(upload_to='images/%Y/%m/%d/')

# class ProductCategory(models.Model):
#     name = models.CharField(max_length=50)

# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     review = models.CharField(max_length=500)
#     # star = models.ForeignKey('Star', on_delete=models.SET_DEFAULT)

# # class Star(models.Model):
# #     star = models.PositiveSmallIntegerField()

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     ordered_date = models.DateTimeField(auto_now_add=True)

# class OrderDetail(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField()
#     # product = models.OneToOneField('Product', on_delete=)



