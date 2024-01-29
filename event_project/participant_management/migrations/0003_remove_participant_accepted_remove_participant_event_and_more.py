# Generated by Django 4.0.2 on 2024-01-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_management', '0002_participant_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AddField(
            model_name='participant',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]