# Generated by Django 3.2.3 on 2021-05-25 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_members',
            name='events_events_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='events.events_events'),
            preserve_default=False,
        ),
    ]
