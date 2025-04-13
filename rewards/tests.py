from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RewardEndpointsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="qweasdzxc#123")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_get_reward_list_empty(self):
        url = reverse("rewards:reward-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_post_reward_request_once_per_day(self):
        url = reverse("rewards:reward-request")

        response = self.client.post(url)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Reward successfully scheduled", response.data["detail"])

        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)
        self.assertIn("only request a reward once per day", response.data["detail"].lower())
