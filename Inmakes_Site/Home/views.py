from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from registration.models import Profile

from .models import InternshipPrograms


# Create your views here.
def home(request):
    purchased_programs = Profile.objects.filter(user_id=request.user.id)
    print('programs :' ,purchased_programs)
    return render(request, 'home.html', {'purchased_programs': purchased_programs})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'aboutus.html')


def internship(request):
    if request.method == 'GET':
        language = request.GET.get('language')
        l_program = InternshipPrograms.objects.filter(lang=language)
    return render(request, 'internship.html', {'l_program': l_program})
