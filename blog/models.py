from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.html import format_html
# Create your models here.
class BlogSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slider_image = models.ImageField(blank=True, null=True, upload_to='about-slider/')
    
    class Meta:
        verbose_name_plural = "Breadcrumb Image"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.slider_image))
    def __str__(self):
        return self.title

class PostAuthor(models.Model):
    auth_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    image = ProcessedImageField(upload_to='authimage/',
                                   processors=[ResizeToFill(40, 40)],
                                   format='JPEG',
                                   options={'quality':80})
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
        
        

class PostCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=80)
    meta_tags = models.CharField(max_length=200)
    description =models.TextField()
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
         
        
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True,)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=155)
    meta_tags = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='blogimage/')
    cat = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(PostAuthor,null=True, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)

            
    class Meta:
        verbose_name_plural = "Blog Comments"
        ordering = ("add_date",)
    def __str__(self):
        return self.name
        
class BlogSeoSnippets(models.Model):
    s_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural = "SEO"
    
    def __str__(self):
        return self.meta_title