from django.db import models

class Image(models.Model):
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.link