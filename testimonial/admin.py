from django.contrib import admin

from testimonial.models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_designatiion', 'image', 'client_message',)
    search_fields = ('client_name',)
    list_per_page = 10


admin.site.register(Testimonial, TestimonialAdmin)