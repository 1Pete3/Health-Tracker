# Generated by Django 4.0 on 2021-12-08 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthTracker', '0003_nutrition'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition',
            name='date',
            field=models.DateField(default=datetime.date(2021, 12, 7)),
        ),
    ]
