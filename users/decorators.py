from django.shortcuts import redirect
from django.contrib import messages

def typing_staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        if hasattr(request.user, 'profile') and request.user.profile.is_typing_staff:
            return view_func(request, *args, **kwargs)

        messages.error(request, 'Access denied. Typing staff only.')
        return redirect('no-access')
    return wrapper

def uploader_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.is_uploader:
            return view_func(request, *args, **kwargs)
        return redirect('no-access')
    return wrapper

def downloader_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.is_downloader:
            return view_func(request, *args, **kwargs)
        return redirect('no-access')
    return wrapper