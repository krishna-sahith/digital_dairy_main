from django.contrib import messages
from django.shortcuts import render
from .models import event_organized


# Create your views here.
def event_form(request):
    return render(request, 'EVENT in/event.html')


def one(request):
    if request.method == 'POST':
        type_of_event = request.POST['type_of_event']
        title_of_event_organized = request.POST['title_of_event_organized']
        name_of_department = request.POST['name_of_department']
        name_of_resource_person = request.POST['name_of_resource_person']
        organized_by = request.POST['organized_by']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']
        faculty_coordinators = request.POST['faculty_coordinators']
        mode = request.POST['mode']
        no_of_faculty_attended = request.POST['no_of_faculty_attended']
        no_of_students_attended_rit = request.POST['no_of_students_attended_rit']
        no_of_students_attended_outside = request.POST['no_of_students_attended_outside']
        total_participants = request.POST['total_participants']
        file_1 = request.POST['file_1']
        file_2 = request.POST['file_2']
        en = event_organized(type_of_event=type_of_event, name_of_department=name_of_department,
                             name_of_resource_person=name_of_resource_person,
                             title_of_event_organized=title_of_event_organized, organized_by=organized_by,
                             from_date=from_date,
                             to_date=to_date, faculty_coordinators=faculty_coordinators, mode=mode,
                             no_of_faculty_attended=no_of_faculty_attended,
                             no_of_students_attended_rit=no_of_students_attended_rit,
                             no_of_students_attended_outside=no_of_students_attended_outside,
                             total_participants=total_participants, file_1=file_1, file_2=file_2)
        try:
            en.save()
            messages.success(request, "Successfully Submitted")
        except:
            messages.error(request, "Submission Failed...Retry")

        return render(request, 'EVENT in/event.html')
