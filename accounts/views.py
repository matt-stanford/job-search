import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .forms import UserRegistrationForm, ResumeForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration has been successful')
            return redirect('search')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('search')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('index')


@login_required(redirect_field_name='next', login_url='login')
def profile(request):
    return render(request, 'accounts/profile.html', {})


@login_required(redirect_field_name='next', login_url='login')
def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # user = request.user
            # form.instance.user = user
            form.save()
            messages.success(request, 'Your resume has been uploaded successfully')
            return redirect('uploadcv')
    else:
        form = ResumeForm()
    return render(request, 'accounts/uploadcv.html', {'form': form})


@login_required(redirect_field_name='next', login_url='login')
def resume_download(request, filepath):
    file_path = os.path.join(settings.MEDIA_ROOT, 'documents', filepath )
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
    



