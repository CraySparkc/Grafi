from datetime import datetime, timedelta, date

import qsstats
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from appname.form import UserProfileForm, UserForm


def index(request):
    dates = []
    for i in range(0,9):
        dates.append(datetime.now() + timedelta(i))
    context = {'values': [['01', dates[1], dates[0], dates[2]],
                          ['02', dates[3], dates[5], dates[4]],
                          ['03', dates[6], dates[8], dates[7]]]}

    return render(request, 'index.html', context)


'''def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'registration/login.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})'''


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your appname account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'registration/login.html', {})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))