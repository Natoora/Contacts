from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from contacts.models import (
    Contact,
    ContactPosition,
    ContactsSettings,
    EmailRecipientList,
)


@admin.register(ContactsSettings)
class ContactsSettingsAdmin(admin.ModelAdmin):
    """
    Contacts Settings Admin.
    """

    fields = [
        "activate_invoice",
        "label_invoice",
        "activate_credit_note",
        "label_credit_note",
        "activate_preparation",
        "label_preparation",
        "activate_confirmation",
        "label_confirmation",
        "activate_market_report",
        "label_market_report",
        "activate_news_letter",
        "label_news_letter",
        "activate_second_selection",
        "label_second_selection",
    ]


class ContactInline(GenericStackedInline):
    """
    Contact inline, for use in customers admin form.
    Includes notification preferences.
    """

    model = Contact
    extra = 0

    fields = (
        "position",
        "first_name",
        "last_name",
        "email",
        "telephone",
        "mobile",
        "notes",
        ("confirmation", "preparation", "invoice", "market_report", "news_letter"),
    )


@admin.register(EmailRecipientList)
class EmailRecipientListAdmin(admin.ModelAdmin):
    """
    EmailRecipientList admin.
    """

    model = EmailRecipientList
    fields = ("name", "description", "recipients")


@admin.register(ContactPosition)
class ContactPositionAdmin(admin.ModelAdmin):
    """
    ContactPosition admin
    """

    model = ContactPosition
    fields = ("name", "sync_to_crm")
