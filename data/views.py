from django.shortcuts import render, redirect
from django.utils import timezone
from . models import CustomUser, Profile,Movie,Video
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import ProfileCreateForm
from . models import Profile
# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("data:profiles")
        return render(request, "index.html")


@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self,request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {
            "profiles": profiles
        }
        return render(request, "profileList.html", context)


@method_decorator(login_required, name="dispatch")
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        #profile creation form
        form = ProfileCreateForm()

        context = {
            "form": form
        }
        return render(request, "profileCreate.html", context)

    def post(self, request, *args, **kwargs):
        form = ProfileCreateForm(request.POST or None)

        context = {
            "form": form
        }

        if form.is_valid():
            #print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect("data:profiles")
        return render(request, "profileCreate.html", context)