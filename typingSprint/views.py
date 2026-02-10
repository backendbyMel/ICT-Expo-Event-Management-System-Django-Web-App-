from django.shortcuts import render,redirect
from .models import Challenger
from django.utils.decorators import method_decorator
from users.decorators import typing_staff_required
from django.contrib.auth.decorators import login_required
from .forms import ChallengerPhotoForm
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    context = {
        'challengers': Challenger.objects.all()
    }
    return render(request,'typingSprint/home.html',context)

def about(request):
    return render(request,'typingSprint/home.html')

class typingSprintListView(ListView):
    model = Challenger
    template_name = 'typingSprint/home.html'
    context_object_name = 'challengers'

    def get_queryset(self):
        return Challenger.objects.order_by(
            '-speed_score',   # highest speed first
            'created_at'      # tie-breaker
        )[:10]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Ranks 11–50
        context['top50'] = Challenger.objects.order_by(
            '-speed_score',
            'created_at'
        )[10:50]

        return context

class typingSprintDetailView(DetailView):
    model = Challenger
    template_name = 'typingSprint/typingSprint_detail.html'

@method_decorator(typing_staff_required, name='dispatch')
class typingSprintCreateView(LoginRequiredMixin, CreateView):
    model = Challenger
    fields = ['name','section','speed_score']
    template_name = 'typingSprint/typingSprint_create.html'

    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        return super().form_valid(form)

@method_decorator(typing_staff_required, name='dispatch')
class typingSprintUpdateView(LoginRequiredMixin, UpdateView):
    model = Challenger
    fields = ['name','section','speed_score']
    template_name = 'typingSprint/typingSprint_create.html'

    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        return super().form_valid(form)
    
@method_decorator(typing_staff_required, name='dispatch')   
class typingSprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Challenger
    success_url = '/'
    template_name = 'typingSprint/typingSprint_delete.html'

    def test_func(self):
        challenger = self.get_object()
        if self.request.user == challenger.created_by:
            return True
        return False

@login_required
@typing_staff_required
def upload_photo(request, pk):
    challenger = Challenger.objects.get(pk=pk)

    if request.method == 'POST':
        form = ChallengerPhotoForm(request.POST, request.FILES, instance=challenger)
        if form.is_valid():
            form.save()
            return redirect('typingSprint-home')
    else:
        form = ChallengerPhotoForm(instance=challenger)

    return render(request, 'typingSprint/upload_photo.html', {'form': form, 'challenger': challenger})