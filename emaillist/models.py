from django.db import models

# Create your models here.
class EmailSubs(models.Model):
    email_id = models.AutoField(primary_key=True)
    emails = models.EmailField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Email Subscribers"
    
    def __str__(self):
        return self.emails
        