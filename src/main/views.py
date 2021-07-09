from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    # form = StudentForm2()
    # context = {
    #     'title': 'title',
    #     'dict_1': { 'django': 'best framework' },
    #     'my_list': [ 2, 3, 4, 5 ],
    #     'template': '<h3>title</h3>',
    #     'form': form 
    # }
    # return render(request, "main/home.html", context)

    return render(request, "main/home.html")


def vehicle_view(request):
    return HttpResponse("This vehicle page")

def login_page(request):
    return HttpResponse("This is login page")

def register_page(request):
    return HttpResponse("This is register page")

def about_view(request):
    return HttpResponse("About Page")


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'main/student_list.html', context)

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form': form
    }
    return render(request, "main/student_add.html", context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student,
    }
    return render(request, "main/student_detail.html", context)

# def student_delete(request, id):
#     # student = Student.objects.get(id=id)
#     student = get_object_or_404(Student, id=id)
#     if request.method == "POST":
#         student.delete()
#         return redirect("list")
    
#     return render(request, "main/student_delete.html")


def student_delete(request, id):
    student = Student.objects.get(id=id)
    # student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("list")
