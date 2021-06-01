from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    date = models.DateTimeField()

    def get_summary(self):
        return self.text[:15]

    def __str__(self):
        return self.title
