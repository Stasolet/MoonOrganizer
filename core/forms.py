from django.forms import ModelForm

from core.models import TextNote, FilmNote, BookNote, ReflectionNote, CalendarNote, LinkNote


# Note forms
class NoteForm(ModelForm):
    class Meta:
        fields = ['title', 'tags']
        labels = {'title': 'Заголовок', 'tags': 'теги'}


class TextNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = TextNote
        fields = ['title', 'text', 'tags']
        labels = {'text': 'Текст'}


class FilmNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = FilmNote
        fields = ['title', 'genre', 'producer', 'duration', 'tags']
        labels = {'title': 'Название фильма', 'genre': 'Жанр', 'producer': 'Продюссерв', 'duration': 'Метраж'}


class BookNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = BookNote
        fields = ['title', 'genre', 'book_author', 'tags']


class ReflectionNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = ReflectionNote
        fields = ['title', 'date', 'reflection', 'tags']


class CalendarNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = CalendarNote
        fields = ['title', 'notification_time', 'event_description', 'start_time', 'end_time', 'tags']


class LinkNoteForm(ModelForm):
    class Meta:
        form = NoteForm
        model = LinkNote
        fields = ['title', 'link', 'tags']
# End Note Forms
