from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Photo
from .forms import PhotoForm, CustomerForm
from users.decorators import uploader_required, downloader_required
from django.contrib.auth.decorators import login_required
from photobooth.utils import add_white_frame
from django.http import HttpResponse

@login_required
def customer_list(request):
    customers = Customer.objects.all().order_by('-id')  # newest first
    return render(request, 'photobooth/customer_list.html', {'customers': customers})

@uploader_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('photobooth_upload', customer_id=customer.id)
    else:
        form = CustomerForm()
    return render(request, 'photobooth/add_customer.html', {'form': form})

@uploader_required
def upload_photos(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        files = request.FILES.getlist('photo')  # <--- Get multiple uploaded files
        for f in files:
            Photo.objects.create(customer=customer, photo=f, uploaded_by=request.user.profile)
        return redirect('customer_photos', customer_id=customer.id)

    form = PhotoForm()
    return render(request, 'photobooth/upload_photos.html', {'form': form, 'customer': customer})

@downloader_required
def customer_photos(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    photos = customer.photos.all().order_by('-uploaded_at')
    return render(request, 'photobooth/customer_photos.html', {'customer': customer, 'photos': photos})

def download_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    
    # Add white frame
    framed_file = add_white_frame(photo.photo, frame_size=50)
    
    # Return as response
    response = HttpResponse(framed_file, content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{photo.photo.name}"'
    return response