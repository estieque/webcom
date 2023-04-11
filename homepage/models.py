from django.db import models
from django.utils.html import format_html
# Create your models here.
class SiteSetting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    meta_description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(blank=True, null=True, max_length=50)
    logo = models.ImageField(blank=True, null=True, upload_to='icon/')
    favicon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.URLField(blank=True, max_length=500)
    discord = models.URLField(blank=True, max_length=500)
    youtube = models.URLField(blank=True, max_length=500)
    contact = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    
class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    slider_image = models.ImageField(blank=True, null=True, upload_to='home-slider/')
    video_url = models.URLField(blank=True, max_length=300)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.slider_image))
    def __str__(self):
        return self.title
        