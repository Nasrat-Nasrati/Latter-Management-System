from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Letter, LetterTracking
from .serializers import LetterSerializer, LetterTrackingSerializer

# List and Create Letters
class LetterListView(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

class LetterCreateView(generics.CreateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

# Retrieve (View) Detail
class LetterDetailView(generics.RetrieveAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

# Update
class LetterUpdateView(generics.UpdateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

# Delete
class LetterDeleteView(generics.DestroyAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

# 🔥 List Tracking Records for a Letter
class LetterTrackingListView(generics.ListAPIView):
    serializer_class = LetterTrackingSerializer

    def get_queryset(self):
        letter_id = self.kwargs['letter_id']
        return LetterTracking.objects.filter(letter_id=letter_id)

# 🔥 Create Tracking Record
class LetterTrackingCreateView(generics.CreateAPIView):
    serializer_class = LetterTrackingSerializer

    def perform_create(self, serializer):
        letter_id = self.kwargs['letter_id']
        letter = get_object_or_404(Letter, id=letter_id)
        serializer.save(letter=letter)
