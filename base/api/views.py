from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import UserSerializer, ResturantSerializer, ProfileSerializer
from base.models import Profile, Resturant
from django.contrib.auth.models import User 
from rest_framework import status

from rest_framework.views import APIView

@api_view(['GET', ])
# @permission_classes([IsAuthenticated])
def getRoutes(request):
    url = "http://127.0.0.1:8000/api/v1/"
    routs = {

        "AUTH": {
            "GET Auth": "http://127.0.0.1:8000/api/auth/",

            "POST Register": "http://127.0.0.1:8000/api/auth/registration/",
            "POST Login": "http://127.0.0.1:8000/api/auth/login/",
            "POST Logout": "http://127.0.0.1:8000/api/auth/logout/",

            "POST auth facebook": "http://127.0.0.1:8000/api/auth/facebook/",
            "POST auth twitter": "http://127.0.0.1:8000/api/auth/twitter/",

            "POST token": "http://127.0.0.1:8000/api/token/",
            "POST token refresh": "http://127.0.0.1:8000/api/token/refresh/",
            "POST token verify": "http://127.0.0.1:8000/api/token/verify/",
        },
        "-----__-----------": "-----__-------",
        "ADMIN":{
            "Admin": "http://127.0.0.1:8000/admin/",
        },
        "----------------": "------------",
        "user":{
            "GET Users All": url + "users/",
            "GET User Object": url + "user/admin",
        },
        "-----------------": "-------------",
        "PROFILE":{
            "GET Profiles All": url + "profiles/",
            "POST Profile Add": url + "profile/add/",
            "GET Profile Object": url + "profile/admin",
            "PUT Profile Edit": url + "profile/edit/pk/",
            "DELETE Profile Delete": url + "profile/delete/pk/",
        },
        "---------------": "-----------",
        "RESTURANT":{
            "GET Resturants All": url + "resturants/",
            "POST Resturant Add": url + "resturant/add/",
            "GET Resturant Object": url + "resturant/pk/",
            "PUT Resturant Edit": url + "resturant/edit/pk/",
            "DELETE Resturant Delete": url + "resturant/delete/pk/",
        },
        
    }
    return Response(routs)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request, username):
    try:
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(
                {"res": "الحساب غير موجود"},
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(
                {"res": "الحساب غير موجود"},
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getResturants(request):
    resturants = Resturant.objects.all()
    serializer = ResturantSerializer(resturants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addResturant(request):
    data = request.data
    user = request.user
    resturant = Resturant.objects.create(
        owner=user,
        name=data['name'],
        phone_number=data['phone_number'],
        address=data['address'],
        location=data['location'],
        logo=data['logo'],
        bio=data['bio'],
        is_delivery=data['is_delivery'],
        is_wallet=data['is_wallet'],
        is_promo_code=data['is_promo_code'],
        discount=data['discount'],
    )
    serializer = ResturantSerializer(resturant, many=False)
    return Response({'message':'Resturant was added!', 'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getResturant(request, pk):
    try:
        resturant = Resturant.objects.get(owner__username=pk)
        serializer = ResturantSerializer(resturant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"res": "المطعم غير موجود"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editResturant(request, pk):
    data = request.data
    user = request.user
    
    resturant = Resturant.objects.get(id=pk)
    if user == resturant.owner:            
        resturant.owner=user
        resturant.name=data['name']
        resturant.phone_number=data['phone_number']
        resturant.address=data['address']
        resturant.location=data['location']
        resturant.logo=data['logo']
        resturant.bio=data['bio']
        resturant.is_delivery=data['is_delivery']
        resturant.is_wallet=data['is_wallet']
        resturant.is_promo_code=data['is_promo_code']
        resturant.discount=data['discount']
        resturant.save()

        serializer = ResturantSerializer(resturant, many=False)
        return Response({'message':'Resturant was updated!', 'data':serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'res':'Get the hell out!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteResturant(request, pk):
    resturant = Resturant.objects.get(id=pk)

    user = request.user
    if user == resturant.owner:    
        resturant.delete()
        return Response({'message':'Resturant was deleted'}, status=status.HTTP_200_OK)
    else:
        return Response({'res':'Get the hell out!'}, status=status.HTTP_400_BAD_REQUEST)












# class ResturantApiView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, username, *args, **kwargs):
#         '''
#         List all the group items for given requested user
#         '''
#         user = request.user

#         resturant = user.resturant

#         serializer = ResturantSerializer(resturant, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def post(self, request, *args, **kwargs):

#         data = {
#             'titel': request.data.get('titel'), 
#             'link': request.data.get('link'), 
#             'created_by': request.user.profile.id,
#             'message': request.data.get('message'), 
#             'data_type': request.data.get('data_type'), 
#             'category': request.data.get('category'), 
#             'sections': request.data.get('sections'), 
#         }

#         serializer = ResturantSerializer(data=data)
#         if serializer.is_valid():
#             data = serializer.save()

            
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
