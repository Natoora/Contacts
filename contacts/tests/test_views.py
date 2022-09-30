from rest_framework.test import APIClient

from common.test.authenticated_client import AuthenticatedClient
from common.test.base_test import NatooraTestCase
from contacts.tests.factories import ContactTestData


class ContactViewsTests(NatooraTestCase):
    """Tests for the Contact viewset"""

    def setUp(self):
        ContactTestData.setup()
        self.client = AuthenticatedClient().normal_client()
        self.uclient = APIClient()

    def test_auth(self):
        response = self.client.get("/api/contacts")
        self.assertEqual(response.status_code, 200)
        response = self.uclient.get("/api/contacts")
        self.assertEqual(response.status_code, 401)

    def test_contact_creation(self):

        info = {
            "app_label": "customers",
            "confirmation": False,
            "content_type": "customer",
            "first_name": "jimmy",
            "invoice": False,
            "last_name": "john",
            "market_report": False,
            "news_letter": False,
            "object_id": 1,
            "position": 1,
            "preparation": False,
            "second_selection": True,
        }

        response = self.client.post("/api/contacts", info)
        self.assertEqual(response.status_code, 201)
