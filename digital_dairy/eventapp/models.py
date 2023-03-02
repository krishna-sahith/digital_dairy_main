from django.db import models


class event_organized(models.Model):
    type_of_event = models.CharField(max_length=20)
    title_of_event_organized = models.CharField(max_length=100,primary_key=True)
    name_of_department = models.CharField(max_length=10)
    name_of_resource_person = models.CharField(max_length=50)
    organized_by = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    faculty_coordinators = models.CharField(max_length=1000)
    mode = models.CharField(max_length=10)
    no_of_faculty_attended = models.IntegerField()
    no_of_students_attended_rit = models.IntegerField()
    no_of_students_attended_outside = models.IntegerField()
    total_participants = models.IntegerField()
    file_1 = models.FileField()
    file_2 = models.FileField()
