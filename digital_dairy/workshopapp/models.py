from django.db import models


class workshop(models.Model):
    Role_workshop = models.CharField(max_length=10)
    Title_workshop = models.CharField(max_length=200, primary_key=True)
    From_date_workshop = models.DateField()
    To_date_workshop = models.DateField()
    Venue_workshop = models.CharField(max_length=200)
    Organized_by_workshop = models.CharField(max_length=200)
    Mode_workshop = models.CharField(max_length=10)
    Image_workshop = models.FileField()
    Certificate_workshop = models.FileField()
