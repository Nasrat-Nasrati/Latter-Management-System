from django.urls import path
from . import views

urlpatterns = [
    path('letters/', views.LetterListView.as_view(), name='letter-list'),
    path('letters/create/', views.LetterCreateView.as_view(), name='letter-create'),
    path('letters/<int:pk>/', views.LetterDetailView.as_view(), name='letter-detail'),
    path('letters/<int:pk>/update/', views.LetterUpdateView.as_view(), name='letter-update'),
    path('letters/<int:pk>/delete/', views.LetterDeleteView.as_view(), name='letter-delete'),

    # 🔥 Letter Tracking Endpoints
    path('letters/<int:letter_id>/trackings/', views.LetterTrackingListView.as_view(), name='letter-tracking-list'),
    path('letters/<int:letter_id>/trackings/create/', views.LetterTrackingCreateView.as_view(), name='letter-tracking-create'),
]
