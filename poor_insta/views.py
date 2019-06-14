from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
from django.views.generic import FormView

from photo_album.settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
from poor_insta.forms import AddPhotoForm, LoginForm
from poor_insta.models import Photo


class HomeView(View):

    def get(self, request):
        photos = Photo.objects.all()
        return render(request, 'poor_insta/base.html', context={'photos':photos})


class AddPhotoView(LoginRequiredMixin, FormView):
    form_class = AddPhotoForm
    template_name = "poor_insta/add_photo.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.cleaned_data.get('photo')
        file = self.request.FILES['photo']
        print(MEDIA_ROOT)
        path = MEDIA_URL + str(file)
        with open(MEDIA_ROOT + str(file), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        Photo.objects.create(user_id=1, path=path)
        return super().form_valid(form)


class LoginView(View):
    def get(self, request):
        return render(request, 'poor_insta/form.html', context = {'form': LoginForm(), 'submit': 'Wbijaj mordo'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_login')
            user_password = form.cleaned_data.get('user_password')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                next = request.GET.get('next')
                if next is not None:
                    return redirect(next)
                return redirect(reverse_lazy('home'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home'))


