from django.db import models
from django.utils.html import format_html
# Create your models here.
class WebApproachSeoSnippets(models.Model):
    s_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural = "SEO"
    
    def __str__(self):
        return self.meta_title
    
    
class WebApproachSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slider_image = models.ImageField(blank=True, null=True, upload_to='about-slider/')
    
    class Meta:
        verbose_name_plural = "Breadcrumb Image"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.slider_image))
    def __str__(self):
        return self.title
    
    
class WebApproachContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='about/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "Web Approach Content"
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.heading
    
    
class FAQ(models.Model):
    content_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "FAQ"
    
    def __str__(self):
        return self.heading