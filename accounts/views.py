from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('search')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        view = super(Register, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


