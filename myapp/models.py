from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=14)
    salary = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    short_description = models.TextField()
    
    def save(self, *args, **kwargs):
        if self.pk:
            original = Employee.objects.get(pk=self.pk)
            if original.salary != self.salary:
                raise ValidationError("Salary cannot be changed once set.")
            if original.designation != self.designation:
                raise ValidationError("Salary cannot be changed once set.")
            
        super().save(*args, **kwargs)

    
