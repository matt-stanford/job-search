from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration has been successful')
            return redirect('search')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
    



