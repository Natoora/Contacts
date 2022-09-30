from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class ContactsSettings(models.Model):
    """
    Contacts Settings.
    """

    activate_confirmation = models.BooleanField(default=True)
    activate_preparation = models.BooleanField(default=True)
    activate_invoice = models.BooleanField(default=True)
    activate_market_report = models.BooleanField(default=True)
    activate_news_letter = models.BooleanField(default=True)
    activate_credit_note = models.BooleanField(default=True)
    activate_second_selection = models.BooleanField(default=True)
    """
    Labels to be displayed on frontend.
    """
    label_confirmation = models.CharField(max_length=100, default="Confirmation")
    label_preparation = models.CharField(max_length=100, default="Preparation")
    label_invoice = models.CharField(max_length=100, default="Invoice")
    label_market_report = models.CharField(max_length=100, default="Market Report")
    label_news_letter = models.CharField(max_length=100, default="News Letter")
    label_credit_note = models.CharField(max_length=100, default="Credit Note")
    label_second_selection = models.CharField(
        max_length=100, default="Second Selection"
    )

    class Meta:
        verbose_name = "Contacts Settings"
        verbose_name_plural = "Contacts Settings"

    def __str__(self):
        return "Contacts Settings"


class Notification(models.Model):
    """
    Specify contact recipients.  Used by orders for
    confirmation, preparation and invoice emails.
    """

    confirmation = models.BooleanField(default=True)
    preparation = models.BooleanField(default=True)
    invoice = models.BooleanField(default=False)
    market_report = models.BooleanField(default=False)
    news_letter = models.BooleanField(default=False)
    credit_note = models.BooleanField(default=False)
    second_selection = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Contact(Notification):
    """
    Generic Contact, can be used in any models.  Inherits Notification
    so that it can be used together in the customers admin form.
    """

    content_type = models.ForeignKey(
        "contenttypes.ContentType", on_delete=models.CASCADE
    )
    object_id = models.CharField(max_length=36)
    content_object = GenericForeignKey()
    position = models.ForeignKey(
        "contacts.ContactPosition", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return "{} - {} {}".format(self.id, self.first_name, self.last_name)

    def full_name(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name, last_name=self.last_name
        )


class EmailRecipientList(models.Model):
    """
    Model to hold a list of recipients for an email
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    recipients = models.TextField(help_text="List of recipients, separated by commas")

    class Meta:
        verbose_name_plural = "Email Recipient Lists"

    def __str__(self):
        return self.name

    def recipients_list(self):
        return self.recipients.split(",")


class ContactPosition(models.Model):
    """
    Model to store Contact Position
    """

    name = models.CharField(max_length=50, unique=True)
    sync_to_crm = models.BooleanField(
        default=False, help_text='E.g. do not sync "Finance" positions to CRM'
    )

    def __str__(self):
        return self.name
