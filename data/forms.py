from django.forms import ModelForm
from . models import Profile


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["uuid"]
        #fields = ["name", "age_limit"]