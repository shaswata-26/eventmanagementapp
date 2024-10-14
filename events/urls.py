from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RSVPViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')  # Explicit basename
router.register(r'events/(?P<event_id>[^/.]+)/rsvp', RSVPViewSet, basename='rsvp')
router.register(r'events/(?P<event_id>[^/.]+)/reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
