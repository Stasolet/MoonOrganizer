import datetime
from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from core.models import FilmNote, CalendarNote, ReflectionNote, BookNote, TextNote, LinkNote
from core.models import MoonNews, WorldNews, WorldNewsCategory
from django.conf import settings


class Command(BaseCommand):
    """Заполнение фиктивными данными через ORM

    количество пользователей заданно в константе
    количество пользователей делающих новости и заметки разные захардкодено
    один пользователь делает и заметки и новости

    где-то увидел, что это говно вариант, типо есть специально для фикстур
    какой-то бедтрип из-за временных зон, пздц, но работет.
    можно сделать улучшенную обработку проверки на режим разработки
    можно вынести заполнение моделей в отдельные функции
    можно добавить вывод в консоль по прогрессу заполнения
    можно добавить аргументы для контроля заполнения"""
    help = 'Add sample data in news and notes'

    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Only in debug mode')
        # очистка базы данных
        User.objects.filter(username__startswith='test').delete()
        WorldNewsCategory.objects.filter(name__startswith='test').delete()
        WorldNews.objects.filter(title__startswith='test').delete()
        MoonNews.objects.filter(title__startswith='test').delete()

        # создание пользователей
        user_count = 6
        notes_count = 5
        users = []
        for u in range(user_count):
            users.append(User.objects.create_user(username=f'test_user{u}',
                                                  password='123'))

        for u in users[:2]:
            for m_n in range(30):
                MoonNews.objects.create(publisher=u,
                                        title=f'test_title moon_news{m_n}',
                                        content='Sample_text  S ' * 30,
                                        tags=f'test {u.username} m_n honor')
        # создание заметок
        notes = defaultdict(list)  # видит Бог я не хотел
        for u in users[1:]:
            for n in range(notes_count):
                notes[TextNote].append(
                    TextNote(
                        creator=u,
                        title=f'Test {u.username} text{n}',
                        tags=f'test text tag{n}',
                        text='Test_sample_text'
                    )
                )
            for n in range(notes_count):
                notes[LinkNote].append(
                    LinkNote(
                        creator=u,
                        title=f'Test {u.username} link{n}',
                        tags=f'test link tag{n}',
                        link='google.com'
                    )
                )
            for n in range(notes_count):
                notes[BookNote].append(
                    BookNote(
                        creator=u,
                        title=f'Test {u.username} book{n}',
                        tags=f'test book tag{n}',
                        book_author='Сладкий бубалех',
                        genre='фантастика'
                    )
                )
            for n in range(notes_count):
                notes[FilmNote].append(
                    FilmNote(
                        creator=u,
                        title=f'Test {u.username} film{n}',
                        tags=f'test film tag{n}',
                        genre='фантастика',
                        duration=FilmNote.DurationChoicer.FEATURE
                    )
                )
            for n in range(notes_count):
                day_delta = datetime.timedelta(days=-1)  # чтобы не были все в один день
                day = datetime.date.today()
                notes[ReflectionNote].append(
                    ReflectionNote(
                        creator=u,
                        title=f'Test {u.username} reflection title{n}',
                        tags=f'test reflection tag{n}',
                        date=day,
                        reflection='Я устал уже делать это заполнение'
                    )
                )
                day += day_delta
            for n in range(notes_count):
                day_delta = datetime.timedelta(days=360)  # чтобы со след года
                day = datetime.datetime.now() + day_delta
                day_delta = datetime.timedelta(days=1)  # чтобы не были все в один день
                notes[CalendarNote].append(
                    CalendarNote(
                        creator=u,
                        title=f'Test {u.username} calendar title{n}',
                        tags=f'test calendar tag{n}',
                        event_description='заполненно',
                        notification_time=day,
                        start_time=day,
                        end_time=day + datetime.timedelta(hours=1)
                    )
                )
                day += day_delta

        for note_model in notes.keys():
            note_model.objects.bulk_create(notes[note_model])

        # добавление подкатегорий пока не реализовано
        parent_cat_labels = ['test_technology', 'test_medic', 'test_music']
        parent_cat = []
        for parent_cat_label in parent_cat_labels:
            p_c = WorldNewsCategory.objects.create(name=parent_cat_label,
                                                   parent_category=None)
            parent_cat.append(p_c)
            p_c: WorldNewsCategory
            news = []
            for w_n in range(20):
                news.append(WorldNews(title=f'test_title world_news{w_n}',
                                      content='sample' * 10,
                                      tags=f'{p_c} test {w_n}',
                                      source_link=f'test_{p_c}_news.com',
                                      categorical=p_c))
            p_c.worldnews_set.bulk_create(news)
