from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    """Базовая абстрактная модель для всех моделей заметок

    содержимого заметки нет"""
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                verbose_name='создатель')
    created = models.DateTimeField(verbose_name='дата создания',
                                   auto_now=True)
    updated = models.DateTimeField(verbose_name='дата создания',
                                   auto_now_add=True)
    title = models.CharField(verbose_name="заголовок",
                             max_length=256)
    tags = models.CharField(verbose_name='теги',
                            max_length=256,
                            blank=True,
                            null=True)
    type_name = 'Заметка'

    class Meta:
        abstract = True
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return f'{self.creator} :: {self._meta.verbose_name} :: {self.title}'


class TextNote(Note):
    text = models.TextField(verbose_name='содержимое',
                            null=True)
    type_name = 'Текстовая'
    detail_url = 'core:textnote_detail'

    class Meta:
        verbose_name = "текстовая заметка"
        verbose_name_plural = "текстовые заметки"

    def get_absolute_url(self):
        return f'note{self.pk}'


class LinkNote(Note):
    link = models.URLField()
    type_name = 'Ссылка'
    detail_url = 'core:linknote_detail'

    class Meta:
        verbose_name = "полезная ссылка"
        verbose_name_plural = "полезные ссылки"


class BookNote(Note):
    title = models.CharField(verbose_name="название книги",
                             max_length=256)
    book_author = models.CharField(verbose_name="автор книги",
                                   max_length=200,
                                   blank=True,
                                   null=True)
    genre = models.CharField(verbose_name="жанр",
                             max_length=100,
                             blank=True,
                             null=True)    # возможна замена на что-то
    type_name = 'Книга'
    detail_url = 'core:booknote_detail'

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"


class FilmNote(Note):
    class DurationChoicer(models.IntegerChoices):
        SHORT = (0, 'Короткий метр')
        FEATURE = (1, 'Полный метр')
        SERIAL = (2, 'Сериал')  # Возможно добавление указание серии и сезона для сериалов
        __empty__ = 'Не выбрано'

    title = models.CharField(verbose_name="название фильма",
                             max_length=256)
    producer = models.CharField(verbose_name="режиссёр",
                                max_length=200,
                                blank=True,
                                null=True)
    genre = models.CharField(verbose_name="жанр",
                             max_length=100,
                             blank=True,
                             null=True)  # возможна замена на что-то
    duration = models.SmallIntegerField(verbose_name='длительность',
                                        choices=DurationChoicer.choices,
                                        null=True,
                                        blank=True)
    type_name = 'Фильм'
    detail_url = 'core:filmnote_detail'

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'


class ReflectionNote(Note):
    """Нужен ли заголовок у данной модели? или его можно заменить датой рефлексии?

    вроде можно даже от TextNote унаследовать избавивгись"""
    date = models.DateField(verbose_name='дата')
    reflection = models.TextField(verbose_name='рефлексия')
    type_name = 'Рефлексия'
    detail_url = 'core:reflectionnote_detail'

    class Meta:
        verbose_name = 'рефлексия'
        verbose_name_plural = 'рефлексии'


class CalendarNote(Note):
    notification_time = models.DateTimeField(verbose_name='время для напоминания')
    event_description = models.TextField(verbose_name='описание события',
                                         null=True,
                                         blank=True)
    start_time = models.DateTimeField(verbose_name='время начала',
                                      null=True,
                                      blank=True)
    end_time = models.DateTimeField(verbose_name='время окончания',
                                    null=True,
                                    blank=True)
    type_name = 'Календарная'
    detail_url = 'core:calendarnote_detail'

    class Meta:
        verbose_name = 'календарная заметка'
        verbose_name_plural = 'календарные заметки'
