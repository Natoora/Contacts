from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contacts.models import Contact, ContactPosition, ContactsSettings
from contacts.serializers import (
    ContactPositionSerializer,
    ContactSerializer,
    ContactsSettingsSerializer,
)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_settings(request):
    """
    Get Contacts Settings.
    """
    settings = ContactsSettings.load()
    settings = ContactsSettingsSerializer(instance=settings)
    return Response(settings.data)


class ContactViewSet(viewsets.ModelViewSet):
    """
    Customer view set
    """

    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        customer = self.request.query_params.get("customer", None)

        if customer:
            return

        return Contact.objects.all()


class ContactPositionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ContactPosition view set
    """

    serializer_class = ContactPositionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ContactPosition.objects.all().order_by("name")
