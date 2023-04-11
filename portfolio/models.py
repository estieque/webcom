from django.db import models
from django.utils.html import format_html
# Create your models here.
class PortfolioSlider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slider_image = models.ImageField(blank=True, null=True, upload_to='about-slider/')
    
    class Meta:
        verbose_name_plural = "Breadcrumb Image"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.slider_image))
    def __str__(self):
        return self.title

class Clients(models.Model):
    cl_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "Client Name"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title
    
class Team(models.Model):
    tm_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Branch of Team"
    
    def __str__(self):
        return self.title

class PortfolioCategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=80)
    meta_tags = models.CharField(max_length=200)
    description =models.TextField()
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "Project Categories"
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.title




class Portfolios(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)
    meta_description = models.CharField(max_length=155)
    meta_tags = models.CharField(max_length=200)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    cat = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null= True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null= True)
    service = models.CharField(max_length=200, null= True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "portfolio Details"
    
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.title
    
    
    
    
class PortfolioSeoSnippets(models.Model):
    s_id = models.AutoField(primary_key=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=200)
    meta_keyword = models.CharField(max_length=200)
    
    
    class Meta:
        verbose_name_plural = "SEO"
    
    def __str__(self):
        return self.meta_title