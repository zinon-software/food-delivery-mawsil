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
    discount = models.FloatField(default=0.00, null=True, blank=True)

    def __str__(self):
        return self.name


# سائق التوصيل
# class Driver(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE)

# class FoodCategory(models.Model): 
#     name = models.CharField(max_length=100, null=True, blank=True)
#     def __str__(self):
#         return self.name

# class Menu(models.Model):
#     created_by = models.ForeignKey(Resturant, null=True, blank=True, on_delete=models.CASCADE, related_name='created_by_resturant')
#     food_category = models.ForeignKey(FoodCategory, null=True, blank=True, on_delete=models.CASCADE, related_name='food_category')
#     titel = models.CharField(max_length=100, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)

# class Payment(models.Model):
#     pass

# class Order(models.Model):
#     

# class OrderDetails(models.Model):
#     pass

