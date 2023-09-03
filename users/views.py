from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Profile
from .serializers import RegisterUserSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = RegisterUserSerializer(data=request.data)

        if data.is_valid():
            new_user = data.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        try:
            profile = Profile.objects.get(user__username=kwargs["username"])
        except Profile.DoesNotExist:
            return Response({"message": "No user exists with this ID"}, status=status.HTTP_404_NOT_FOUND)

        serialized_data = ProfileSerializer(profile)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
