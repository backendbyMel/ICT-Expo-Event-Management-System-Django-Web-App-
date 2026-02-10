from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('typingSprint-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # ✅ saves to DB
            profile = user.profile
            profile.is_typing_staff = form.cleaned_data['is_typing_staff']
            profile.is_cashier = form.cleaned_data['is_cashier']
            profile.is_uploader = form.cleaned_data['is_uploader']
            profile.is_downloader = form.cleaned_data['is_downloader']
            profile.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def logout_page(request):
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def no_access(request):
    return render(request, 'users/no_access.html')