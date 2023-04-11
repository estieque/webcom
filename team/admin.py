from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TeamMember
# Register your models here.


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'position', 'image_tag', 'email')
    
admin.site.register(TeamMember, TeamMemberAdmin)