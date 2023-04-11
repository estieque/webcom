from django.contrib import admin

from homepage.models import SiteSetting, Slider

# Register your models here.

admin.site.register(SiteSetting)



class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'short_description', 'video_url')
    search_fields = ('name',)
    
admin.site.register(Slider, SliderAdmin)