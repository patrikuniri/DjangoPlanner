# Generated by Django 4.0.2 on 2024-01-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_management', '0004_participant_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.CharField(default='Default Event', max_length=100),
        ),
    ]
