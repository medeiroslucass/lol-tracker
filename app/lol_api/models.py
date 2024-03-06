from django.db import models

class Champion(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name

