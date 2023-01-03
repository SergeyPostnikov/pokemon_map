from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon", 
        verbose_name='Parent',
        related_name="next_evolution",
        on_delete=models.CASCADE,
        blank=True, null=True)

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
    level = models.IntegerField(verbose_name="Level", blank=True, default=0)
    health = models.IntegerField(verbose_name="Health", blank=True, default=0)
    strength = models.IntegerField(verbose_name="Strength", blank=True, default=0)
    defence = models.IntegerField(verbose_name="Defence", blank=True, default=0)
    stamina = models.IntegerField(verbose_name="Stamina", blank=True, default=0)

    def __str__(self):
        return f'{self.kind.title} entity'
