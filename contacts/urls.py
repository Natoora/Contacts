from django.urls import include, re_path
from rest_framework import routers

from contacts import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"contacts", views.ContactViewSet, basename="contacts")
router.register(
    r"contact-positions", views.ContactPositionViewSet, basename="contact-positions"
)

urlpatterns = [
    re_path(r"", include(router.urls)),
    re_path(r"contacts-settings", views.get_settings),
]
