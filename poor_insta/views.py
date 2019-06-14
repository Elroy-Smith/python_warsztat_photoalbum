from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
from django.views.generic import FormView

from photo_album.settings import STATIC_ROOT
from poor_insta.forms import AddPhotoForm


class HomeView(View):
    def get(self, request):
        return render(request, 'poor_insta/base.html')

class AddPhotoView(FormView):
    form_class = AddPhotoForm
    template_name = "poor_insta/add_photo.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.cleaned_data.get('photo')
        file = self.request.FILES['photo']
        print(STATIC_ROOT)
        with open(STATIC_ROOT + '/' + str(file), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)