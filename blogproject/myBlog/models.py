from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)  # Title of the blog post
    tagline = models.CharField(max_length=500, blank=True)  # Short tagline
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Featured image
    content = models.TextField()  # No word limit for content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto timestamp on update

    def __str__(self):
        return self.title
