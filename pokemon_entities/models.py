from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    kind = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE, 
        verbose_name='Pokemon', 
        blank=True,
        null=True)
    latitude = models.FloatField(verbose_name="Lat")
    longitude = models.FloatField(verbose_name="Lon")
    appeard_at = models.DateTimeField(
        verbose_name="Appeard at",
        blank=True, null=True)
    disappeard_at = models.DateTimeField(
        verbose_name="Disappeard at", 
        blank=True, null=True)
