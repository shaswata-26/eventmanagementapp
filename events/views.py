from rest_framework import viewsets
from .models import Event, RSVP, Review
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer


from rest_framework import permissions as p1 # Correct import

from . import permissions as p2

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()  # Define the queryset
    serializer_class = EventSerializer
    permission_classes = [p1.IsAuthenticated | p2.IsOrganizer]

    def get_queryset(self):
        # Optional: filter for public events
        return Event.objects.filter(is_public=True)

class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()  # Define the queryset
    serializer_class = RSVPSerializer
    permission_classes = [p1.IsAuthenticated]

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.kwargs['event_id'])
        serializer.save(event=event, user=self.request.user.userprofile)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Define the queryset
    serializer_class = ReviewSerializer
    permission_classes = [p1.IsAuthenticated]

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.kwargs['event_id'])
        serializer.save(event=event, user=self.request.user.userprofile)

