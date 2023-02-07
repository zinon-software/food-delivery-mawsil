from django.db import models
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField  
from phone_field import PhoneField 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(default='', upload_to="avatars", blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    is_driver = models.BooleanField(default=False, null=True, blank=True)

# المطعم
class Resturant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=200, null=True, blank=True)
    location = LocationField(null=True, blank=True)  
    logo = models.ImageField(default='', upload_to="logos", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_delivery = models.BooleanField(default=False, null=True, blank=True)
    is_wallet = models.BooleanField(default=False, null=True, blank=True)
    is_promo_code = models.BooleanField(default=False, null=True, blank=True)
    discount = models.DecimalField(default=0.00,max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


# سائق التوصيل
# class Driver(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)

class FoodCategory(models.Model): 
    created_by = models.ForeignKey(Resturant, null=True, blank=True, on_delete=models.CASCADE, related_name='by_resturant')
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Menu(models.Model):
    created_by = models.ForeignKey(Resturant, null=True, blank=True, on_delete=models.CASCADE, related_name='created_by_resturant')
    food_category = models.ForeignKey(FoodCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='food_category')
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='placeholder.png')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    resturant = models.ForeignKey(Resturant, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


# class Payment(models.Model):
#     pass

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)