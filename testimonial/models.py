from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.html import format_html
# Create your models here.
class Testimonial(models.Model):
    tmo_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=200)
    client_designatiion = models.CharField(max_length=200)
    image = ProcessedImageField(upload_to='clients/',
                                   processors=[ResizeToFill(60, 60)],
                                   format='JPEG',
                                   options={'quality':80})
    client_message = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Testimonial"
        
        
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.client_name