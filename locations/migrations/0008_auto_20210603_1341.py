# Generated by Django 3.2.3 on 2021-06-03 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210603_1341'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0007_alter_locations_locations_owner_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=255)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('occupied_from', models.DateTimeField()),
                ('occupied_to', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.room')),
            ],
        ),
        migrations.RemoveField(
            model_name='locations_locations',
            name='owner_id',
        ),
        migrations.RemoveField(
            model_name='locations_rooms',
            name='locations_locations',
        ),
        migrations.DeleteModel(
            name='Locations_Events',
        ),
        migrations.DeleteModel(
            name='Locations_Locations',
        ),
        migrations.DeleteModel(
            name='Locations_Rooms',
        ),
    ]