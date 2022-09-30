from django.core.validators import validate_email

from common.test.base_test import NatooraTestCase
from contacts.tests.factories import ContactFactory


class TestNotificationAndContact(NatooraTestCase):
    """
    Test Contact and Notification models.
    Notification model is abstract and so is part of
    the Contact table.
    """

    def setUp(self):
        self.contact = ContactFactory()

    """
    Attributes
    """

    def test_position(self):
        self.assertEquals(type(self.contact.position.name), str)

    def test_first_name(self):
        self.assertEquals(type(self.contact.first_name), str)

    def test_last_name(self):
        self.assertEquals(type(self.contact.last_name), str)

    def test_email(self):
        self.assertIsNone(validate_email(self.contact.email))

    def test_telephone(self):
        self.assertEquals(type(self.contact.telephone), str)

    def test_mobile(self):
        self.assertEquals(type(self.contact.mobile), str)

    def test_notes(self):
        self.assertEquals(type(self.contact.notes), str)

    """
    Notification preferences
    """

    def test_confirmation(self):
        self.assertEquals(type(self.contact.confirmation), bool)

    def test_preparation(self):
        self.assertEquals(type(self.contact.preparation), bool)

    def test_invoice(self):
        self.assertEquals(type(self.contact.invoice), bool)

    def test_market_report(self):
        self.assertEquals(type(self.contact.market_report), bool)

    def test_news_letter(self):
        self.assertEquals(type(self.contact.news_letter), bool)

    def test_credit_note(self):
        self.assertEquals(type(self.contact.credit_note), bool)

    def test_second_selection(self):
        self.assertEquals(type(self.contact.second_selection), bool)
