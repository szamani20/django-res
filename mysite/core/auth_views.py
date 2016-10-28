from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import RegistrationForm


def login(request):
    if request.user.is_authenticated():
        return redirect('core:home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            redirect_url = request.GET.get('next', reverse('core:home'))
            auth_login(request, form.get_user())
            return HttpResponseRedirect(redirect_url)

    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html',
                  context={'login_form': form})


def register(request):
    if request.user.is_authenticated():
        return redirect('core:home')

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')

    else:
        form = RegistrationForm()

    return render(request, 'auth/register.html',
                  context={'register_form': form})


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    return redirect('core:home')
