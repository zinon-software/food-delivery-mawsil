from rest_framework.serializers import ModelSerializer 
from base.models import Profile, Resturant
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'id'] 

class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta: 
        model = Profile
        fields = '__all__'

class ResturantSerializer(ModelSerializer):
    class Meta: 
        model = Resturant
        fields = '__all__'