from common.test.authenticated_client import AuthenticatedClient
from common.test.base_test import NatooraTestCase
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from contacts.tests.factories import ContactTestData
from suppliers.tests.factories import SupplierTestData


class TestContactViewSet(NatooraTestCase):
    """
    tests Contacts only view
    """

    def setUp(self):
        ContactTestData().setup()
        self.contact = Contact.objects.first()
        self.json = ContactSerializer(self.contact)
        self.client = AuthenticatedClient().normal_client()
        SupplierTestData().setup_suppliers()

    def test_correct_get(self):
        response = self.client.get("/api/contacts")
        number_of_contacts = Contact.objects.count()
        self.assertEqual(len(response.data), number_of_contacts)
        self.assertEqual(response.status_code, 200)

    def test_correct_post(self):
        response = self.client.post(
            "/api/contacts",
            {
                "first_name": "Giacomo",
                "last_name": "Brunetti",
                "email": "g@gmail.com",
                "telephone": "0044 1234 567890",
                "mobile": None,
                "object_id": 1,
                "position": 1,
                "notes": None,
                "confirmation": False,
                "preparation": False,
                "invoice": True,
                "market_report": True,
                "news_letter": True,
                "credit_note": True,
                "second_selection": False,
                "content_type": "supplier",
                "app_label": "suppliers",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_wrong_post(self):
        response = self.client.post("/api/contacts", {"name": 445})
        self.assertNotEqual(response.status_code, 200)

    def test_correct_put(self):
        response = self.client.put(
            "/api/contacts/{}".format(self.contact.id),
            {
                "first_name": "Giacomo",
                "last_name": "Brunetti",
                "email": "g@gmail.com",
                "telephone": "0044 1234 567890",
                "mobile": None,
                "object_id": 1,
                "position": 1,
                "notes": None,
                "confirmation": False,
                "preparation": False,
                "invoice": True,
                "market_report": True,
                "news_letter": True,
                "credit_note": True,
                "second_selection": True,
                "content_type": "supplier",
                "app_label": "suppliers",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_wrong_put(self):
        response = self.client.put(
            "/api/contacts/{}".format(self.contact.id),
            {
                # removed first_name should break it
                # 'first_name': 'Giacomo',
                "last_name": "Brunetti",
                "email": "g@gmail.com",
                "telephone": "0044 1234 567890",
                "mobile": None,
                "object_id": 1,
                "position": "Tractor Chauffeur",
                "notes": None,
                "confirmation": False,
                "preparation": False,
                "invoice": True,
                "market_report": True,
                "news_letter": True,
                "credit_note": True,
                "second_selection": True,
                "content_type": "supplier",
                "app_label": "suppliers",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        before = Contact.objects.count()
        response = self.client.delete("/api/contacts/{}".format(self.contact.id))
        after = Contact.objects.count()
        self.assertEqual(response.status_code, 204)
        self.assertLess(after, before)
