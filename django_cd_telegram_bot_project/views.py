import asyncio
import sys
from django import middleware
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dzDjango.bot import Base, main, engine
from dzDjango.models import ModelMila
@csrf_exempt
def reg(request):
class Post(ModelMila.Model):

ModelMila
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
        asyncio.run(main())
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = ModelMila.objects.all()
        return HttpResponse(data)
    return render(request, 'login.html')

def webhook(request):
    # Преобразование запроса от Telegram в объект Update
    update = Update.de_json(request.body.decode('utf-8'), context.bot)


