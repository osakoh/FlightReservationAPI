from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token

from . import views


class TestFlight(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view = views.FlightViewSet.as_view({'get': 'list'})
        self.uri = '/api/flights/'

    @staticmethod
    def setup_user():
        user = get_user_model()
        return user.objects.create_user(username='test6',
                                        password='test',
                                        email='t@t.com')

    def test_list(self):
        """
        test the list of flight
        """
        user = self.setup_user()
        token = user.auth_token.key
        # adds the appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))


