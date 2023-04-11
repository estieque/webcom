from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from gallery.models import Gallery, GallerySeoSnippets, GallerySlider

# Register your models here.
class GallerySliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(GallerySlider, GallerySliderAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(Gallery, GalleryAdmin)



class GallerySeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('meta_title',)
    list_per_page = 10
    
admin.site.register(GallerySeoSnippets, GallerySeoSnippetsAdmin)