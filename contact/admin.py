from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from contact.models import ContactMessage, ContactSeoSnippets, ContactSlider

# Register your models here.
class ContactSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(ContactSlider, ContactSliderAdmin)


class ContactSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('title',)
admin.site.register(ContactSeoSnippets, ContactSeoSnippetsAdmin)



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message', 'location')
    search_fields = ('name',)
    
admin.site.register(ContactMessage, ContactMessageAdmin)