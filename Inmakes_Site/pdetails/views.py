from django.shortcuts import render
from .models import Levelperprogram, Contents
from Home.models import InternshipPrograms


# Create your views here.


def level(request, id):
    program = InternshipPrograms.objects.get(id=id)
    level = Levelperprogram.objects.filter(c_name=id)
    return render(request, 'level.html', {'level': level, 'program': program})


def details(request, id, lid):
    program = InternshipPrograms.objects.get(id=id)
    level = Levelperprogram.objects.filter(id=lid)
    return render(request, 'details.html', {'program': program, 'level': level})


def chapter_details(request, lid):
    contents = Contents.objects.filter(level_per_program_id=lid)
    return render(request, 'chapter_details.html', {'contents': contents})
