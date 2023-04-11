from django.contrib import admin
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

from about.models import AboutContentOne, AboutContentTwo, AboutSeoSnippets, AboutSlider, ProgressBar

# Register your models here.

admin.site.unregister(Attachment)
admin.site.unregister(Group)

class AboutSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(AboutSlider, AboutSliderAdmin)

class AboutContentOneAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'sub_heading', 'image_tag',)
    search_fields = ('title',)
    summernote_fields = ('content',)
    list_per_page = 10
    
admin.site.register(AboutContentOne, AboutContentOneAdmin)


class AboutContentTwoAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'sub_heading', 'image_tag',)
    search_fields = ('title',)
    summernote_fields = ('content',)
    list_per_page = 10
    
admin.site.register(AboutContentTwo, AboutContentTwoAdmin)



class ProgressBarAdmin(SummernoteModelAdmin):
    list_display = ('title', 'value',)
    search_fields = ('title',)
admin.site.register(ProgressBar, ProgressBarAdmin)



class AboutSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('title',)
admin.site.register(AboutSeoSnippets, AboutSeoSnippetsAdmin)