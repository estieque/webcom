from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from services.models import Service, ServiceSeoSnippets, ServiceSlider

# Register your models here.
class ServiceSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('title',)
admin.site.register(ServiceSeoSnippets, ServiceSeoSnippetsAdmin)


class ServiceSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(ServiceSlider, ServiceSliderAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'image_tag', 'description',)
    
admin.site.register(Service, ServiceAdmin)