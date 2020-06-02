from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {})


@login_required
def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            form.instance.user = user
            form.save()
            messages.success(request, 'Your resume has been uploaded successfully')
            return redirect('uploadcv')
    else:
        form = ResumeForm()
    return render(request, 'accounts/uploadcv.html', {'form': form})
    



