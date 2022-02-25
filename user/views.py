from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.utils.translation import gettext as _


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    extra_context = {'title': _("Registration Form")}
    template_name = 'user/register.html'


def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error!"))
            return redirect('login')

    else:
        return render(
            request,
            'user/login.html',
            {
                "title": _("Authorisation Form"),
            }
        )


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')


"""
def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(
        request,
        'user/register.html',
        {
            'form': form,
            "title": _("Registration Form"),
        }
    )
"""
