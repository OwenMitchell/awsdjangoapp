from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.template import loader
from .forms import CustomUserCreationForm


class Login(LoginView):
    template_name = "registration/login.html"
    next_page = '/account/profile'


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/account/')
    template = loader.get_template('account/profile.html')
    return HttpResponse(template.render({}, request))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Change to the appropriate redirect URL
            return redirect('/account/profile/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})
