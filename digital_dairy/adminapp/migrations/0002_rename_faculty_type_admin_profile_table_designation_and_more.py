# Generated by Django 4.1.7 on 2023-03-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin_profile_table',
            old_name='Faculty_Type',
            new_name='Designation',
        ),
        migrations.RemoveField(
            model_name='admin_profile_table',
            name='Student_Year',
        ),
        migrations.RemoveField(
            model_name='admin_profile_table',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin_profile_table',
            name='Email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
