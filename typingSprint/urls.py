from django.urls import path
from . import views
from .views import (typingSprintListView, 
                    typingSprintDetailView,
                    typingSprintCreateView,
                    typingSprintUpdateView,
                    typingSprintDeleteView)


urlpatterns = [
    path('', typingSprintListView.as_view(), name="typingSprint-home"),
    path('typingSprint/<int:pk>', typingSprintDetailView.as_view(), name="typingSprint-detail"),
    path('typingSprint/create', typingSprintCreateView.as_view(), name="typingSprint-create"),
    path('typingSprint/<int:pk>/update', typingSprintUpdateView.as_view(), name="typingSprint-update"),
    path('typingSprint/<int:pk>/delete', typingSprintDeleteView.as_view(), name="typingSprint-delete"),
    path('about/',views.about, name="typingSprint-about"),
    path('upload_photo/<int:pk>/', views.upload_photo, name='upload_photo'),
    
]