from django.contrib import admin
from .models import Account_Users, Accounts_Teams, Accounts_Teams_Has_Accounts_Users


admin.site.register(Account_Users)
admin.site.register(Accounts_Teams)
admin.site.register(Accounts_Teams_Has_Accounts_Users)
