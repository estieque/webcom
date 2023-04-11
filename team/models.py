from email.mime import image
from django.db import models
from django.utils.html import format_html
# Create your models here.
class TeamMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True, max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='teamimage/')
    facebook = models.URLField(blank=True, max_length=500)
    instagram = models.URLField(blank=True, max_length=500)
    twitter = models.URLField(blank=True, max_length=500)
    youtube = models.URLField(blank=True, max_length=500)
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.member_name