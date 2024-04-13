from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, AddingForm
from .models import Adding
# Create your views here. 

def authen(request):
    if request.user.is_authenticated:
        return redirect('adding')

    context = {
        'form' : LoginForm()
    }
    return render(request,'authen.html', context=context)

def adding(request):
    if request.user.is_authenticated:
        form = AddingForm()
        KNOW_CHOICES = form.fields.get('fromWhereKnows')._choices
        print()
        if request.method == "POST":
            form = AddingForm(request.POST)
            if form.is_valid():
                form.save()
                form = AddingForm()
            else:
                print('N')
        context = {
            'KNOW_CHOICES' : KNOW_CHOICES,
            'form' : form,
        }
        return render(request, 'adding.html', context=context)
    return redirect('index')

def info(request):
    if request.user.is_authenticated:

        addings = Adding.objects.all()

        context = {
            'addings' : addings,
        }
        return render(request, 'info.html', context=context)

    return redirect('index')


def info_detail(request, pk):
    if request.user.is_authenticated:
        object = Adding.objects.get(pk=pk)
        info = [
            ('Имя', object.name),
            ('discord id', object.discord_id),
            ('Откуда узнал про сервер', object.getKnows()),
        ]

        context = {
            'info' : info,
            'pk' : pk
        }
        return render(request, 'detail.html', context=context)

    return redirect('index')

def adding_delete(request, pk):
    print('delete')
    Adding.objects.get(pk=pk).delete()
    return redirect('info')