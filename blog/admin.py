from django.contrib import admin
from .models import BlogSeoSnippets, BlogSlider, Comments, PostCategory, BlogPost, PostAuthor
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class BlogSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(BlogSlider, BlogSliderAdmin)


class BlogSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('meta_title',)
    list_per_page = 10
    
admin.site.register(BlogSeoSnippets, BlogSeoSnippetsAdmin)



class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'image_tag')
    search_fields = ('name',)
    
admin.site.register(PostAuthor, PostAuthorAdmin)

class PostCategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'meta_description', 'cat_slug', 'image_tag', 'add_date')
    search_fields = ('title',)
    summernote_fields = ('description',)
    list_per_page = 10


admin.site.register(PostCategory, PostCategoryAdmin)

class BlogpostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'image_tag', 'add_date')
    search_fields = ('title',)
    summernote_fields = ('content',)
    list_per_page = 10



admin.site.register(BlogPost, BlogpostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content',)
    search_fields = ('name', 'email',)

admin.site.register(Comments, CommentsAdmin)