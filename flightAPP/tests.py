from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token

from . import views


def setup_user():
    user = get_user_model()
    return user.objects.create_user(username='test6',
                                    password='test',
                                    email='t@t.com')


class TestFlight(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view = views.FlightViewSet.as_view({'get': 'list', 'post': 'create'})
        self.uri = '/api/flights/'

    def test_list(self):
        """
        test the list of flight
        """
        user = setup_user()
        token = user.auth_token.key
        # adds the appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_post_flight(self):
        user = setup_user()
        token = user.auth_token.key
        # adds the appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        data = {
            "flight_number": "ATS-BTN",
            "operating_airline": "AirTravels",
            "departure_city": "STN",
            "arrival_city": "FRT",
            "date_of_departure": "2021-06-20",
            "estimated_time_of_departure": "21:30:00"
        }
        response = self.client.post(self.uri, data=data)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'.format(response.status_code))
