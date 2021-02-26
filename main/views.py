from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Register

# Create your views here.

def home(response):
    return render(response, "main/index.html", {"users":Register.objects.all()})

def register(response):
    if response.method == "POST":
        name = response.POST.get("name")
        last_name = response.POST.get("last")
        email = response.POST.get("email")
        r = Register(name=name, last_name=last_name, email=email)
        r.save()
        return HttpResponseRedirect("/")
    return render(response, "main/register.html", {})