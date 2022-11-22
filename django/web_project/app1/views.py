from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
from .forms import LoginForm, RandNum
from django.urls import reverse

from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#from .forms import ContactForm
#from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

'''

def reg(request):
    return HttpResponse('<h1>Генератор случайных чисел</h1>')



def guests(request):
       
        error = ''
        if request.method == 'POST':
           form = RegistrationForm(request.POST)
           if form.is_valid():
                form.save()
           else:
                error = 'Ошибка'
        form = RegistrationForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'guests.html', data)

'''


'''
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
          #  return redirect('login')
    else:
        form=UserLoginForm()
    return render(request, 'login.html', {"form": form})

'''

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/randomizer/')
                else:
                    return render(request,
                          'account/disabled_password.html')
            else:
                return render(request,
                          'account/disabled_password.html')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def get_num(request):
    submitbutton = request.POST.get("submit")

    leftNum = ''
    rightNum = ''
    countNum = ''
    rand_list=[]
    rez=''

    form = RandNum(request.POST)
    if form.is_valid():
        leftNum = form.cleaned_data.get("leftNum")
        rightNum = form.cleaned_data.get("rightNum")
        countNum = form.cleaned_data.get("countNum")

        for i in range(countNum):
            rand_list.append(randint(leftNum, rightNum))
            rez+=str(rand_list[i])
            rez+=" "

      #  rez = rand_list
        #rez = {"rand_list": rand_list}

    context = {'form': RandNum, 'leftNum': leftNum,
               'rightNum': rightNum, 'submitbutton': submitbutton,
               'countNum': countNum, 'rez': rez}



    return render(request, 'randomizer.html', context)



