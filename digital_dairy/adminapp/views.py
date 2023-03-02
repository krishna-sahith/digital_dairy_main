from django.contrib import messages
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
        Designation = request.POST['Designation']
        en = admin_profile_table(Name=name, Email=email, Password_Admin_Profile=password, Department=department,
                                 Contact_Number=contact, Designation=Designation)
        try:
            en.save()
            messages.success(request,"Succcessfullt Submitted")
        except:
            messages.error(request, "Submission Failed")

        return render(request, 'ADMIN/Admin_profile.html')
