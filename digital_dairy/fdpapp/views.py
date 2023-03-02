from django.contrib import messages
from django.shortcuts import render
from .models import FDP_table


# Create your views here.
def fdp_form(request):
    return render(request, 'FDP in/FDP.html')


def one(request):
    if request.method == 'POST':
        type_of_person_FDP = request.POST['type_of_person_FDP']
        name_of_FDP = request.POST['name_of_FDP']
        from_date_FDP = request.POST['from_date_FDP']
        to_date_FDP = request.POST['to_date_FDP']
        organized_by_FDP = request.POST['organized_by_FDP']
        sponsorship_FDP = request.POST['sponsorship_FDP']
        photo_FDP = request.POST['photo_FDP']
        certificate_FDP = request.POST['certificate_FDP']
        en = FDP_table(type_of_person_FDP=type_of_person_FDP, name_of_FDP=name_of_FDP, from_date_FDP=from_date_FDP,
                       to_date_FDP=to_date_FDP, organized_by_FDP=organized_by_FDP, sponsorship_FDP=sponsorship_FDP,
                       photo_FDP=photo_FDP,
                       certificate_FDP=certificate_FDP)
        try:
            en.save()
            messages.success(request, "Succcessfullt Submitted")
        except:
            messages.error(request, "Submission Failed")

        return render(request, 'FDP in/FDP.html')
