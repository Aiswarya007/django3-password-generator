from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    # return HttpResponse('<h1>Hello there!!!</h1>')
    return render(request, 'generator/home.html')
    # return render(request, 'generator/home.html',
    #               {'password': 'vdcjwdcbe'})


def password(request):

    # thepassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # length = 10
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',
                  {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')