from django.db import models
import random


class Tweet(models.Model):
    # id = modes.AutoField(primary_key=True)
    content = models.TextField()
    image = models.FileField(upload_to='tweets_img', blank=True, null=True)


    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
