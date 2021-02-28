# Generated by Django 3.1.6 on 2021-02-11 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('core', '0001_initial'), ('core', '0002_auto_20210206_1349'), ('core', '0003_auto_20210206_1354'), ('core', '0004_auto_20210206_1604'), ('core', '0005_worldnews_categorical'), ('core', '0006_auto_20210206_1822')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('book_title', models.CharField(max_length=256, verbose_name='название книги')),
                ('book_author', models.CharField(max_length=200, verbose_name='автор книги')),
                ('genre', models.CharField(max_length=100, verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
        migrations.CreateModel(
            name='CalendarNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('notification_time', models.DateTimeField(verbose_name='время для напоминания')),
                ('event_description', models.TextField(verbose_name='описание события')),
                ('start_time', models.DateTimeField(verbose_name='время начала')),
                ('end_time', models.DateTimeField(verbose_name='время окончания')),
            ],
            options={
                'verbose_name': 'календарная заметка',
                'verbose_name_plural': 'календарные заметки',
            },
        ),
        migrations.CreateModel(
            name='FilmNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('film_title', models.CharField(max_length=256, verbose_name='название фильма')),
                ('producer', models.CharField(max_length=200, verbose_name='режиссёр')),
                ('genre', models.CharField(max_length=100, verbose_name='жанр')),
                ('duration', models.SmallIntegerField(choices=[(0, 'Короткий метр'), (1, 'Полный метр'), (2, 'Сериал')], verbose_name='длительность')),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
        ),
        migrations.CreateModel(
            name='LinkNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'полезная ссылка',
                'verbose_name_plural': 'полезные ссылки',
            },
        ),
        migrations.CreateModel(
            name='MoonNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('published', models.DateTimeField(auto_now=True, verbose_name='дата публикации')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
            ],
            options={
                'verbose_name': 'Новость ресурса',
                'verbose_name_plural': 'Новости ресурса',
                'ordering': ['-published'],
                'get_latest_by': 'published',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReflectionNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('date', models.DateField(verbose_name='дата')),
                ('reflection', models.TextField(verbose_name='рефлексия')),
            ],
            options={
                'verbose_name': 'рефлексия',
                'verbose_name_plural': 'рефлексии',
            },
        ),
        migrations.CreateModel(
            name='TextNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='заголовок')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'текстовая заметка',
                'verbose_name_plural': 'текстовые заметки',
            },
        ),
        migrations.CreateModel(
            name='WorldNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('published', models.DateTimeField(auto_now=True, verbose_name='дата публикации')),
                ('tags', models.CharField(max_length=256, null=True, verbose_name='теги')),
                ('source_link', models.URLField()),
            ],
            options={
                'verbose_name': 'Новость из мира',
                'verbose_name_plural': 'Новости из мира',
                'ordering': ['-published'],
                'get_latest_by': 'published',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorldNewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256, verbose_name='категория')),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.worldnewscategory', verbose_name='родительская категория')),
            ],
            options={
                'verbose_name': 'Категория нововстей',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
        migrations.AddIndex(
            model_name='worldnews',
            index=models.Index(fields=['published'], name='core_worldn_publish_72c296_idx'),
        ),
        migrations.AddField(
            model_name='textnote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='reflectionnote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='moonnews',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='linknote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='filmnote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='calendarnote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='booknote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddIndex(
            model_name='moonnews',
            index=models.Index(fields=['published'], name='core_moonne_publish_70d54f_idx'),
        ),
        migrations.RemoveField(
            model_name='booknote',
            name='book_title',
        ),
        migrations.RemoveField(
            model_name='filmnote',
            name='film_title',
        ),
        migrations.AlterField(
            model_name='booknote',
            name='book_author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='автор книги'),
        ),
        migrations.AlterField(
            model_name='booknote',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='booknote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='booknote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='название книги'),
        ),
        migrations.AlterField(
            model_name='calendarnote',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время окончания'),
        ),
        migrations.AlterField(
            model_name='calendarnote',
            name='event_description',
            field=models.TextField(blank=True, null=True, verbose_name='описание события'),
        ),
        migrations.AlterField(
            model_name='calendarnote',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время начала'),
        ),
        migrations.AlterField(
            model_name='calendarnote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='calendarnote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='duration',
            field=models.SmallIntegerField(choices=[(0, 'Короткий метр'), (1, 'Полный метр'), (2, 'Сериал')], null=True, verbose_name='длительность'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='genre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='producer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='режиссёр'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='название фильма'),
        ),
        migrations.AlterField(
            model_name='linknote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='linknote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='reflectionnote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='reflectionnote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='textnote',
            name='tags',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='textnote',
            name='title',
            field=models.CharField(max_length=256, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='duration',
            field=models.SmallIntegerField(choices=[(None, 'Не выбрано'), (0, 'Короткий метр'), (1, 'Полный метр'), (2, 'Сериал')], null=True, verbose_name='длительность'),
        ),
        migrations.RenameField(
            model_name='worldnewscategory',
            old_name='category',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='filmnote',
            name='duration',
            field=models.SmallIntegerField(blank=True, choices=[(None, 'Не выбрано'), (0, 'Короткий метр'), (1, 'Полный метр'), (2, 'Сериал')], null=True, verbose_name='длительность'),
        ),
        migrations.AlterField(
            model_name='moonnews',
            name='published',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='textnote',
            name='text',
            field=models.TextField(null=True, verbose_name='содержимое'),
        ),
        migrations.AddField(
            model_name='worldnews',
            name='categorical',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.worldnewscategory', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='worldnews',
            name='published',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='worldnews',
            name='source_link',
            field=models.URLField(verbose_name='источник'),
        ),
    ]