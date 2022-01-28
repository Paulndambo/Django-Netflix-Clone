from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def home(request):
    current_year = timezone.now().year
    context = {
        "current_year": current_year
    }
    return render(request, "index.html", context)