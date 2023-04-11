from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from portfolio.models import Clients, PortfolioSeoSnippets, Portfolios, PortfolioCategory, PortfolioSlider, Team
# Register your models here.
class PortfolioSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    
admin.site.register(PortfolioSlider, PortfolioSliderAdmin)


class PortfolioCategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'meta_description', 'slug', 'image_tag', 'add_date')
    search_fields = ('title',)
    summernote_fields = ('description',)
    list_per_page = 10


admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag',)
    search_fields = ('title',)
    list_per_page = 10


admin.site.register(Clients, ClientsAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 10


admin.site.register(Team, TeamAdmin)


class PortfoliosAdmin(SummernoteModelAdmin):
    list_display = ('title','image_tag',)
    summernote_fields = ('descriptions',)
    search_fields = ('title',)
    list_per_page = 10
    
admin.site.register(Portfolios, PortfoliosAdmin)


class PortfolioSeoSnippetsAdmin(SummernoteModelAdmin):
    list_display = ('meta_title', 'meta_description', 'meta_keyword',)
    search_fields = ('meta_title',)
    list_per_page = 10
    
admin.site.register(PortfolioSeoSnippets, PortfolioSeoSnippetsAdmin)
    