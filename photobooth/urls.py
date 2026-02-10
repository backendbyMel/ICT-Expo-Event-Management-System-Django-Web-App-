from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:customer_id>/', views.upload_photos, name='photobooth_upload'),
    path('photos/<int:customer_id>/', views.customer_photos, name='customer_photos'),
    path('add-customer/', views.add_customer, name='photobooth-add_customer'),
    path('customers/', views.customer_list, name='photobooth-customer_list'),
    path('photo/download/<int:photo_id>/', views.download_photo, name='download_photo'),
]