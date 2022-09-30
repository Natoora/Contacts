from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from contacts.models import Contact, ContactPosition, ContactsSettings
from contacts.services.phone_number_utils import parse_phone_number


class ContactsSettingsSerializer(serializers.ModelSerializer):
    """
    VOIP settings serializer.
    """

    class Meta:
        model = ContactsSettings
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


class ContactSerializer(serializers.ModelSerializer):
    """
    Contacts Serializer
    """

    content_type = serializers.CharField(write_only=True, required=True)
    app_label = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Contact
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "telephone",
            "mobile",
            "object_id",
            "position",
            "notes",
            "confirmation",
            "preparation",
            "invoice",
            "market_report",
            "news_letter",
            "credit_note",
            "content_type",
            "app_label",
            "second_selection",
        )

    def create(self, validated_data):
        model = validated_data.get("content_type", None)
        app_label = validated_data.get("app_label", None)
        c = Contact()
        c.object_id = validated_data.get("object_id")
        c.content_type = ContentType.objects.get(model=model, app_label=app_label)
        c.first_name = validated_data.get("first_name")
        c.last_name = validated_data.get("last_name")
        c.email = validated_data.get("email")
        c.telephone = validated_data.get("telephone")
        c.mobile = validated_data.get("mobile")
        c.position = validated_data.get("position")
        c.notes = validated_data.get("notes")
        c.confirmation = validated_data.get("confirmation")
        c.preparation = validated_data.get("preparation")
        c.invoice = validated_data.get("invoice", False)
        c.market_report = validated_data.get("market_report", False)
        c.news_letter = validated_data.get("news_letter", False)
        c.credit_note = validated_data.get("credit_note", False)
        c.second_selection = validated_data.get("second_selection", False)
        c.save()
        return c

    def update(self, instance, validated_data):
        model = validated_data.get("content_type", None)
        app_label = validated_data.get("app_label", None)
        instance.object_id = validated_data.get("object_id", instance.object_id)
        instance.content_type = (
            ContentType.objects.get(model=model, app_label=app_label)
            if model and app_label
            else instance.content_type
        )
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.telephone = validated_data.get("telephone", instance.telephone)
        instance.mobile = validated_data.get("mobile", instance.mobile)
        instance.position = validated_data.get("position", instance.position)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.confirmation = validated_data.get(
            "confirmation", instance.confirmation
        )
        instance.preparation = validated_data.get("preparation", instance.preparation)
        instance.invoice = validated_data.get("invoice", instance.invoice)
        instance.market_report = validated_data.get(
            "market_report", instance.market_report
        )
        instance.news_letter = validated_data.get("news_letter", instance.news_letter)
        instance.credit_note = validated_data.get("credit_note", instance.credit_note)
        instance.second_selection = validated_data.get(
            "second_selection", instance.second_selection
        )
        instance.save()
        return instance

    def validate_mobile(self, value):
        """Try to parse number to E164 standard.

        :param value: Mobile number received by serializer.
        :return: Parsed mobile number.
        """
        if value:
            parsed, tel = parse_phone_number(value)
            if parsed:
                return tel
            else:
                raise serializers.ValidationError("Invalid mobile number")

    def validate_telephone(self, value):
        """Try to parse number to E164 standard.

        :param value: Telephone number received by serializer.
        :return: Parsed telephone number.
        """
        if value:
            parsed, tel = parse_phone_number(value)
            if parsed:
                return tel
            else:
                raise serializers.ValidationError("Invalid telephone number")


class ContactPositionSerializer(serializers.ModelSerializer):
    """
    ContactPosition Serializer
    """

    class Meta:
        model = ContactPosition
        fields = ("id", "name", "sync_to_crm")
