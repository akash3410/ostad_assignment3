from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import UpdateForm

# Create your views here.
def home_page(request):
    employes = Employee.objects.all()
    return render(request, "index.html", {"employes": employes})

def delete_em(request, pk):
    employes = Employee.objects.get(pk=pk)
    employes.delete()
    return redirect("home_page")

def update_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = UpdateForm(instance=employee)

    return render(request, 'update_emp.html', {'form': form})