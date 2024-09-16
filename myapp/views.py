from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def home_page(request):
    employes = Employee.objects.all()
    return render(request, "index.html", {"employes": employes})

def delete_em(request, pk):
    employes = Employee.objects.get(pk=pk)
    employes.delete()
    return redirect("home_page")