from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.v1.serializers import AccountProfileSerializer


class AccountProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Retrieve authenticated user profile",
        responses={200: AccountProfileSerializer},
    )
    def get(self, request):
        serializer = AccountProfileSerializer(request.user)
        return Response(serializer.data)
