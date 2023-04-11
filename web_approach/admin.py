from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from web_approach.models import FAQ, WebApproachContent, WebApproachSeoSnippets, WebApproachSlider

# Register your models here.
class WebApproachSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(WebApproachSlider, WebApproachSliderAdmin)

class WebApproachContentAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'content', 'image_tag',)
    search_fields = ('title',)
    summernote_fields = ('content',)
    list_per_page = 10
    
admin.site.register(WebApproachContent, WebApproachContentAdmin)



class WebApproachSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('title',)
admin.site.register(WebApproachSeoSnippets, WebApproachSeoSnippetsAdmin)

class FAQAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'content',)
    search_fields = ('heading',)
    summernote_fields = ('content',)
admin.site.register(FAQ, FAQAdmin)