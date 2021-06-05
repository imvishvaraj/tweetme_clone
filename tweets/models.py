from django.db import models


class Tweet(models.Model):
    # id = modes.AutoField(primary_key=True)
    content = models.TextField()
    image = models.FileField(upload_to='tweets_img', blank=True, null=True)
