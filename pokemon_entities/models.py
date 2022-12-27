from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title
