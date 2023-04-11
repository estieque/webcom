from django.db import models

# Create your models here.
class HeaderScript(models.Model):
    s_id = models.AutoField(primary_key=True)
    script = models.TextField()
    
    class Meta:
        verbose_name_plural = "Insert Header Script"
    
    def __str__(self):
        return self.script
    
    
class FooterScript(models.Model):
    s_id = models.AutoField(primary_key=True)
    script = models.TextField()
    
    class Meta:
        verbose_name_plural = "Insert Footer Script"
    
    def __str__(self):
        return self.script
    