# Generated by Django 5.1.4 on 2024-12-18 10:15

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_account_email_account_is_staff_account_is_superuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
