from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from myapp.models import Employee
# Create your views here.
def home(request):
    employes = Employee.objects.all()
    return render(request, "accounts/home.html", {"employes": employes})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration")
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/registration.html", context)

def login_view(request):
    employes = Employee.objects.all()
    emp = {}
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            for employee in employes:
                if user == employee.name:
                    user = user
                    emp = employee
                    break
            login(request, user)
            return redirect("account_home")
    else:
        form = AuthenticationForm()
        
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)
    