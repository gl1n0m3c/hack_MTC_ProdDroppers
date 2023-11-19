from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.serializers import (
    UserSerializer,
    FriendsSerializer,
    FriendsWaitingSerializer,
)
from users.models import FriendsAssepted, FriendsNotAssepted


class UserDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)


class UserFriendsAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsAssepted.objects.filter(user1=pk).values()
        return Response({"friends": list(friends)})


class UserFriendsWaitingAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        friends = FriendsNotAssepted.objects.get_friends(pk)

        return Response(FriendsWaitingSerializer(friends).data)
