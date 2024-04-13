from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("its okay")

def login_view(request):
    if(request.POST):
        # имя формы, которое скорее всего надо добавлять в forms.py
        yourForm= Zalupa(request.POST)
        # имя поля
        itemValue = yourForm[''].value()
        print(itemValue)
        # Check if you get the value
        return HttpResponse(itemValue )
    else:
        return render(request, "adding.html")