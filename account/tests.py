from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthTokenTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", email="user@example.com", password="qweasdzxc#123"
        )

    def test_get_jwt_token(self):
        data = {"username": "test_user", "password": "qweasdzxc#123"}
        response = self.client.post("/api/v1/account/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        response = self.client.post(
            "/api/v1/account/token/refresh/",
            {
                "refresh": str(refresh),
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_token_verify(self):
        refresh = RefreshToken.for_user(self.user)
        access = str(refresh.access_token)
        response = self.client.post("/api/v1/account/token/verify/", {"token": access})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileViewTests(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username="test_user", email="user@example.com", password="qweasdzxc#123"
        )
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_get_profile_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.get("/api/v1/account/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "test_user")
        self.assertEqual(response.data["email"], "user@example.com")
        self.assertEqual(response.data["coins"], 0)

    def test_get_profile_unauthenticated(self):
        response = self.client.get("/api/v1/account/profile/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
