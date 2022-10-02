import factory
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyChoice

from contacts.models import (
    ContactsSettings,
    Notification,
    EmailRecipientList,
    Contact,
    ContactPosition,
)


class ContactsSettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactsSettings

    activate_confirmation = factory.Faker("pybool")
    activate_preparation = factory.Faker("pybool")
    activate_invoice = factory.Faker("pybool")
    activate_market_report = factory.Faker("pybool")
    activate_news_letter = factory.Faker("pybool")
    activate_credit_note = factory.Faker("pybool")
    activate_second_selection = factory.Faker("pybool")

    label_confirmation = FuzzyText(length=10)
    label_preparation = FuzzyText(length=10)
    label_invoice = FuzzyText(length=10)
    label_market_report = FuzzyText(length=10)
    label_news_letter = FuzzyText(length=10)
    label_credit_note = FuzzyText(length=10)
    label_second_selection = FuzzyText(length=10)
    created_at = timezone.now()


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    confirmation = factory.Faker("pybool")
    preparation = factory.Faker("pybool")
    invoice = factory.Faker("pybool")
    market_report = factory.Faker("pybool")
    news_letter = factory.Faker("pybool")
    credit_note = factory.Faker("pybool")
    second_selection = factory.Faker("pybool")


class ContactPositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactPosition
        django_get_or_create = ("name",)

    name = factory.Faker("name")
    sync_to_crm = factory.Faker("pybool")


class ContactFactory(NotificationFactory):
    class Meta:
        model = Contact
        django_get_or_create = ("last_name",)

    content_type = factory.Iterator(ContentType.objects.all())
    object_id = FuzzyInteger(low=0, high=100)
    position = factory.SubFactory(
        ContactPositionFactory,
        name=FuzzyChoice(["Operations Manager", "Consultant", "Baker"]),
    )
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")
    email = factory.Faker("email")
    telephone = factory.Faker("phone_number")
    mobile = factory.Faker("phone_number")
    notes = FuzzyText(length=40)


class EmailRecipientListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailRecipientList

    name = factory.Faker("name")
    description = FuzzyText(length=100)
    recipients = FuzzyText(length=100)
