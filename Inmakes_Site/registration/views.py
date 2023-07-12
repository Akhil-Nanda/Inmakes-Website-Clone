from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        place = request.POST['place']
        qualification = request.POST['qualification']
        program = request.POST['program']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'user already registered with same course!!')
            return redirect('registration:register')
        else:
            user = User.objects.create_user(first_name=first_name, email=email, username=email, password='123456')
            user.save()
            user_details = Profile.objects.create(user_id=user.id, phone_number=phone_number, place=place,
                                                  qualification=qualification,
                                                  program_id=program)
            user_details.save()
            return redirect('registration:login')
    return render(request, 'register.html', {messages: 'messages'})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return redirect('registration:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('registration:login')
