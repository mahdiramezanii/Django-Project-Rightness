# Generated by Django 4.0.3 on 2022-03-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount', '0003_rename_father_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='power',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]