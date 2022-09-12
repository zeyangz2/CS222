from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("welcome to new project")

def user_list(request):
    # find user_list.html in app1 dir in templates folder
    return render(request, "user_list.html")