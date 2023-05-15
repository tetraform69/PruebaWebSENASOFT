from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    return render(request, "login.html")

def formNewEmpleado(request):
    return render(request, "newEmpleado.html")