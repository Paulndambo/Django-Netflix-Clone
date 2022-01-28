from django.shortcuts import render
from django.utils import timezone
from . models import CustomUser, Profile,Movie,Video
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
