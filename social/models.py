from django.db import models

class About(models.Model):
    about_title = models.CharField(max_length=20)
    about_description = models.TextField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'About'
    
    def __str__(self):
        return self.about_title

class SocialLink(models.Model):
    platform = models.CharField(max_length=20)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform