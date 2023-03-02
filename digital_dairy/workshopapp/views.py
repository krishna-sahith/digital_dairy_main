from django.contrib import messages
from django.shortcuts import render
from .models import workshop


# Create your views here.
def workshop(request):
    return render(request, 'WORKSHOP in/workshop.html')


def one(request):
    if request.method == 'POST':
        Role_workshop = request.POST['Role_workshop']
        Title_workshop = request.POST['Title_workshop']
        From_date_workshop = request.POST['From_date_workshop']
        To_date_workshop = request.POST['To_date_workshop']
        Venue_workshop = request.POST['Venue_workshop']
        Organized_by_workshop = request.POST['Organized_by_workshop']
        Mode_workshop = request.POST['Mode_workshop']
        Image_workshop = request.POST['Image_workshop']
        Certificate_workshop = request.POST['Certificate_workshop']

        en = workshop(Role_workshop=Role_workshop, Title_workshop=Title_workshop, From_date_workshop=From_date_workshop,
                      To_date_workshop=To_date_workshop, Venue_workshop=Venue_workshop,
                      Organized_by_workshop=Organized_by_workshop,
                      Mode_workshop=Mode_workshop, Image_workshop=Image_workshop,
                      Certificate_workshop=Certificate_workshop,)
        try:
            en.save()
            messages.success(request, "Succcessfullt Submitted")
        except:
            messages.error(request, "Submission Failed")

        return render(request, 'WORKSHOP in/workshop.html')
