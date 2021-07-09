from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm, StudentForm2

# Create your views here.

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    form = StudentForm2()
    context = {
        'title': 'title',
        'dict_1': { 'django': 'best framework' },
        'my_list': [ 2, 3, 4, 5 ],
        'template': '<h3>title</h3>',
        'form': form 
    }
    return render(request, "main/home.html", context)


def vehicle_view(request):
    return HttpResponse("This vehicle page")

def login_page(request):
    return HttpResponse("This is login page")

def register_page(request):
    return HttpResponse("This is register page")

def about_view(request):
    return HttpResponse("About Page")

