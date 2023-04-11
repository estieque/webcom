from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.html import format_html
# Create your models here.
class ServiceSeoSnippets(models.Model):
    s_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural = "SEO"
    
    def __str__(self):
        return self.meta_title
    
class ServiceSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slider_image = models.ImageField(blank=True, null=True, upload_to='service-slider/')
    
    class Meta:
        verbose_name_plural = "Breadcrumb Image"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.slider_image))
    def __str__(self):
        return self.title
    
    
class Service(models.Model):
    ser_id = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=200)
    description = models.TextField()
    icon = ProcessedImageField(upload_to='service/',
                                   processors=[ResizeToFill(100, 100)],
                                   format='PNG',
                                   options={'quality':80})
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Our Services"
        
        
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.icon))
    
    def __str__(self):
        return self.service_title