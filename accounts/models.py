from django.db import models


class Accounts_Teams(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Account_Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=45)


class Accounts_Teams_Has_Accounts_Users(models.Model):
    role = models.CharField(max_length=45)
    accounts_teams_id = models.ForeignKey('Accounts_Teams', on_delete=models.CASCADE)
    accounts_users_id = models.ForeignKey('Account_Users', on_delete=models.CASCADE)
