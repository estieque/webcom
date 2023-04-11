from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from scripts.models import FooterScript, HeaderScript
# Register your models here.
class HeaderScriptAdmin(SummernoteModelAdmin):
    list_display = ('script',)
    summernote_fields = ('script',)
admin.site.register(HeaderScript, HeaderScriptAdmin)



class FooterScriptAdmin(SummernoteModelAdmin):
    list_display = ('script',)
    summernote_fields = ('script',)
admin.site.register(FooterScript, FooterScriptAdmin)