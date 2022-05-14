from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import UserSerializer, ResturantSerializer, ProfileSerializer
from base.models import Profile, Resturant
from django.contrib.auth.models import User 
from rest_framework import status

from rest_framework.views import APIView

@api_view(['GET', ])
@permission_classes([])
def getRoute(request):
    url = "http://127.0.0.1:8000/api/v1/"
    routs = {
        "Admin": "http://127.0.0.1:8000/admin/",
        "-----__-----------": "-----__-------",
        "Register": url + "register/",
        "Login": url + "login/",
        "----------------": "------------",
        "Users->": url + "users/",
        "User": url + "user/admin",
        "-----------------": "-------------",
        "Profiles->": url + "profiles/",
        "Profile": url + "profile/admin",
        "---------------": "-----------",
        "Resturants->": url + "resturants/",
        "Resturant": url + "resturant/admin",
    }
    return Response(routs)



@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
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
def getProfiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
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
def getResturants(request):
    resturants = Resturant.objects.all()
    serializer = ResturantSerializer(resturants, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getResturant(request, username):
    try:
        resturant = Resturant.objects.get(owner__username=username)
        serializer = ResturantSerializer(resturant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(
                {"res": "المطعم غير موجود"},
                status=status.HTTP_400_BAD_REQUEST
            )



class ResturantApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username, *args, **kwargs):
        '''
        List all the group items for given requested user
        '''
        user = request.user

        resturant = user.resturant

        serializer = ResturantSerializer(resturant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'titel': request.data.get('titel'), 
            'link': request.data.get('link'), 
            'created_by': request.user.profile.id,
            'message': request.data.get('message'), 
            'data_type': request.data.get('data_type'), 
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }

        serializer = ResturantSerializer(data=data)
        if serializer.is_valid():
            data = serializer.save()

            
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
