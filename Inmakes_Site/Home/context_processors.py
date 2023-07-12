from .models import InternshipPrograms, Language


def programs(request):
    program = InternshipPrograms.objects.all()
    return dict(program=program)


def language(request):
    language = Language.objects.all()
    return dict(language=language)
