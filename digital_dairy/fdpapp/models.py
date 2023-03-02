from django.db import models


class FDP_table(models.Model):
    type_of_person_FDP = models.CharField(max_length=20)
    name_of_FDP = models.CharField(max_length=100, primary_key=True)
    from_date_FDP = models.DateField()
    to_date_FDP = models.DateField()
    organized_by_FDP = models.CharField(max_length=100)
    sponsorship_FDP = models.CharField(max_length=30)
    photo_FDP = models.FileField()
    certificate_FDP = models.FileField()
