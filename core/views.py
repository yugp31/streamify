from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import MediaContent
from .forms import SignUpForm, MediaContentForm

class HomeView(ListView):
    model = MediaContent
    template_name = 'core/home.html'
    context_object_name = 'media_list'
    ordering = ['-uploaded_at']
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related('uploader')

class MediaDetailView(DetailView):
    model = MediaContent
    template_name = 'core/media_detail.html'
    context_object_name = 'media'

    def get_queryset(self):
        return super().get_queryset().select_related('uploader').prefetch_related('comments__user')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'core/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

class UploadMediaView(LoginRequiredMixin, CreateView):
    model = MediaContent
    form_class = MediaContentForm
    template_name = 'core/upload_media.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

