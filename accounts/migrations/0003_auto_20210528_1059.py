# Generated by Django 3.2.3 on 2021-05-28 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210528_1059'),
        ('locations', '0006_alter_locations_locations_owner_id'),
        ('accounts', '0002_auto_20210525_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts_teams_has_accounts_users',
            name='accounts_teams_id',
        ),
        migrations.RemoveField(
            model_name='accounts_teams_has_accounts_users',
            name='accounts_users_id',
        ),
        migrations.DeleteModel(
            name='Account_Users',
        ),
        migrations.DeleteModel(
            name='Accounts_Teams',
        ),
        migrations.DeleteModel(
            name='Accounts_Teams_Has_Accounts_Users',
        ),
    ]
