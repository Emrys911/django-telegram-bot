import asyncio

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_cd_telegram_bot_project import (static)
@csrf_exempt
def reg(request):
    mila = index()
    if request.method == 'POST':
        mila.pole = 'Hello world'
        mila.email = request.POST['email']
        mila.password = request.POST['password']
        mila.save()
        return HttpResponse('Email'+' '+mila.email+' '+"успешно зарегистрирован!")
    return render(request, 'mila.html')

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print('Bot started!')
        asyncio.run(index())
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = index.objects.all()
        return HttpResponse(data)
    return render(request)