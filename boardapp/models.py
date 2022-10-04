from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    post_image = models.ImageField(upload_to="")
    like = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    readtxt = models.TextField(blank=True)

    def __str__(self):
        return self.title

