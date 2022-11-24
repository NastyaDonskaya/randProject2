from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm, RandNum, UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Numbers
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






def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username='username', password='password')
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

    leftNum = 0
    rightNum = 0
    countNum = 0


    rand_list=[]
    rez=''

    form = RandNum(request.POST)
    if form.is_valid():
        leftNum = form.cleaned_data.get("leftNum")
        rightNum = form.cleaned_data.get("rightNum")
        countNum = form.cleaned_data.get("countNum")
        if leftNum>rightNum:
            return redirect('error1')
        for i in range(countNum):
            rand_list.append(randint(leftNum, rightNum))
            rez+=str(rand_list[i])
            if (i!=countNum-1):
                rez += ","
                rez+=" "
    Numbers.objects.create(user_name=request.user.username, left_num=leftNum, right_num=rightNum,
    count_num=countNum, rand_num = rez)
    context = {'leftNum': leftNum, 'rightNum': rightNum, 'countNum': countNum, 'submitbutton': submitbutton,
    'rez': rez, 'form': RandNum}

    return render(request, 'randomizer.html', context)






def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()

            return redirect('http://127.0.0.1:8000/app1/accounts/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def error(request):
    return render(request, "error1.html")

def history(request):
    context  = {
            'numbers': Numbers.objects.filter(user_name=request.user.username)
        }

    return render(request, 'history.html', context)