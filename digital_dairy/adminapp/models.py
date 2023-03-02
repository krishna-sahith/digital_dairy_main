from django.db import models


class admin_profile_table(models.Model):
    Name = models.CharField(max_length=50)
    Password_Admin_Profile = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,primary_key=True)
    Department = models.CharField(max_length=10)
    Contact_Number = models.IntegerField(max_length=10)
    Designation = models.CharField(max_length=10)
