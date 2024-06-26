from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

# Register your models here.
class AccountAdmin(UserAdmin):
    
    list_display = ('email','first_name','last_name','username','date_joined')
    list_display_links = ('email','first_name','last_name')
    
    readonly_fields = ('last_login','date_joined')
    ordering = ('username',)
    filter_horizontal = ()
    list_filter = ()
    field_sets = ()

admin.site.register(CustomUser,AccountAdmin)