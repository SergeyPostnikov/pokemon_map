from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название англ.")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название яп.")
    image = models.ImageField(upload_to='media', blank=True, verbose_name="Картинка")
    description = models.TextField(verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey(
        "Pokemon", 
        verbose_name='Предыдущая эволюция',
        related_name="next_evolutions",
        on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, 
        on_delete=models.CASCADE, 
        verbose_name='Вид',
        related_name='entities', 
        blank=True,
        null=True)
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(
        verbose_name="Возник",
        blank=True, null=True)
    disappeared_at = models.DateTimeField(
        verbose_name="Исчез", 
        blank=True, null=True)
    level = models.IntegerField(verbose_name="Уровень", blank=True)
    health = models.IntegerField(verbose_name="Здоровье", blank=True)
    strength = models.IntegerField(verbose_name="Сила", blank=True)
    defence = models.IntegerField(verbose_name="Защита", blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость", blank=True)

    def __str__(self):
        return f'Экземпляр {self.kind.title}'
