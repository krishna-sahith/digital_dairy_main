from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import admin_profile_table


# Create your views here.
def admin_profile(request):
    return render(request, 'ADMIN/Admin_profile.html')


def one(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        department = request.POST['department']
        contact = request.POST['contact']
        faculty = request.POST['faculty']
        year = request.POST['year']
        en = admin_profile_table(Name=name, Email=email, Password_Admin_Profile=password, Department=department,
                                 Contact_Number=contact, Faculty_Type=faculty, Student_Year=year)
        en.save()
        n = "done"
        return render(request, 'ADMIN/Admin_profile.html', {'n': n})
