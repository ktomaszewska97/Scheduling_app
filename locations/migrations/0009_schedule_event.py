# Generated by Django 3.2.3 on 2021-06-07 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_description'),
        ('locations', '0008_auto_20210603_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
            preserve_default=False,
        ),
    ]
