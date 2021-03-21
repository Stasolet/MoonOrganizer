from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    """Базовый класс для новостей

    от него унаследуются новости ресурса и парсинг других общемировых
    В будущем возможно добавятся картинки для заголовка"""
    title = models.CharField(verbose_name='заголовок', max_length=256)
    content = models.TextField(verbose_name='содержимое')
    published = models.DateTimeField(verbose_name='дата публикации', auto_now=True, null=True)
    tags = models.CharField(verbose_name='теги', max_length=256, null=True)

    class Meta:
        abstract = True
        ordering = ['-published']
        get_latest_by = 'published'
        indexes = [models.Index(fields=['published'])]

    def __str__(self):
        return self.title


class MoonNews(News):
    """Новости ресурса"""
    publisher = models.ForeignKey(User,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  verbose_name='Автор')

    class Meta(News.Meta):
        verbose_name = 'Новость ресурса'
        verbose_name_plural = 'Новости ресурса'

    def get_absolute_url(self):
        return reverse('core:moonnews-detail', kwargs={'pk': self.id})


class WorldNewsCategory(models.Model):  # возможно от подкатегорий для новостей откажусь
    name = models.CharField(max_length=256, verbose_name='категория')
    parent_category = models.ForeignKey('self',
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name='родительская категория')

    class Meta:
        verbose_name = 'Категория нововстей'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.name


class WorldNews(News):
    """Аггрегированные новости с других ресурсов

    механизм их получения требует разработки и данная модель может уйти в небытие
    взамен неё может быть модель, содержащая список парсеров для разных сайтов, с аггрегацией
    на стороне клиента"""
    source_link = models.URLField(verbose_name='источник')
    categorical = models.ForeignKey(WorldNewsCategory,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='категория')

    class Meta(News.Meta):
        verbose_name = 'Новость из мира'
        verbose_name_plural = 'Новости из мира'
