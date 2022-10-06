from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    post_image = models.ImageField(upload_to="")
    like = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtxt = models.TextField(null=True, blank=True, default=" ")

    def __str__(self):
        return self.title

