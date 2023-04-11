from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import EmailSubs

# Register your models here.
class EmailSubsAdmin(admin.ModelAdmin):
    list_display = ('emails',)
    list_per_page = 20
    
admin.site.register(EmailSubs,EmailSubsAdmin)