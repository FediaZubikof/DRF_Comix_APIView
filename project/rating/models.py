from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Comic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Название комикса')
    author = models.CharField(max_length=100, verbose_name='Автор комикса')
    rating = models.ForeignKey(
        'Rating',
        on_delete=models.CASCADE,
        related_name='value+',
        verbose_name='Рейтинг комикса',
    )

    def __str__(self):
        return self.title


class Rating(models.Model):
    comic_id = models.IntegerField(verbose_name='Ссылка на комикс')
    user_id = models.IntegerField(verbose_name='Идентификатор пользователя оценившего комикс')
    value = models.SmallIntegerField(
        validators=[MaxValueValidator(5),
                    MinValueValidator(1)],
        verbose_name='Оценка пользователя от 1 до 5',
    )
