from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Value, CharField
from django.db.models.functions import Left
from django.forms import ModelForm
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from core.models import MoonNews
from core.models import TextNote, BookNote, LinkNote, FilmNote, ReflectionNote, CalendarNote, AVAILABLE_NOTES
from django.contrib.auth.forms import UserCreationForm

# todo template for change password
# todo reset password
# todo registration
# todo шаблон для формы с наследованием управлением выводом


# Note block
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


# Notes Add
class NoteAdd(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('core:notes')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.creator = self.request.user
        note.save()
        return super().form_valid(form)


class TextNoteAdd(NoteAdd):
    form_class = TextNoteForm
    template_name = 'core/textnote_form.html'


class FilmNoteAdd(NoteAdd):
    form_class = FilmNoteForm
    template_name = 'core/filmnote_form.html'


class BookNoteAdd(NoteAdd):
    form_class = BookNoteForm
    template_name = 'core/note_form.html'


class ReflectionNoteAdd(NoteAdd):
    form_class = ReflectionNoteForm
    template_name = 'core/note_form.html'


class CalendarNoteAdd(NoteAdd):
    form_class = CalendarNoteForm
    template_name = 'core/note_form.html'


class LinkNoteAdd(NoteAdd):
    form_class = LinkNoteForm
    template_name = 'core/note_form.html'
# End Notes add


# Notes change
class NoteChange(UpdateView):
    success_url = reverse_lazy('core:notes')


class TextNoteChange(NoteChange):
    model = TextNote
    form_class = TextNoteForm


class LinkNoteChange(NoteChange):
    model = LinkNote
    form_class = LinkNoteForm


class FilmNoteChange(NoteChange):
    model = FilmNote
    form_class = FilmNoteForm


class BookNoteChange(NoteChange):
    model = BookNote
    form_class = BookNoteForm


class ReflectionNoteChange(NoteChange):
    model = ReflectionNote
    form_class = ReflectionNoteForm


class CalendarNoteChange(NoteChange):
    model = CalendarNote
    form_class = CalendarNoteForm
# End Notes change


# Notes delete
class NoteDelete(DeleteView):
    success_url = reverse_lazy('core:notes')
    template_name = 'core/delete_note.html'


class TextNoteDelete(NoteDelete):
    model = TextNote


class LinkNoteDelete(NoteDelete):
    model = LinkNote


class BookNoteDelete(NoteDelete):
    model = BookNote


class FilmNoteDelete(NoteDelete):
    model = FilmNote


class ReflectionNoteDelete(NoteDelete):
    model = ReflectionNote


class CalendarNoteDelete(NoteDelete):
    model = CalendarNote


# End Notes delete


# Notes Watch
# todo Для некоторых заметок не требуется детальный вид(ссылки) для рефлексии надо ещё выводить дату рефлексии
class NotesListView(LoginRequiredMixin, ListView):
    paginate_by = 12
    template_name = "core/notes.html"

    def get_queryset(self):
        u = self.request.user
        n = AVAILABLE_NOTES[0].objects\
            .filter(creator=u)\
            .order_by()\
            .annotate(type_name=Value(AVAILABLE_NOTES[0].type_name, output_field=CharField()),
                      detail_url=Value(AVAILABLE_NOTES[0].detail_url, output_field=CharField()))\
            .values_list('id', 'title', 'type_name', 'detail_url', 'created', 'updated', 'tags', named=True)
        query_list = []
        for m in AVAILABLE_NOTES[1:]:
            query_list.append(m.objects.filter(creator=u).order_by()
                              .annotate(type_name=Value(m.type_name, output_field=CharField()),
                                        detail_url=Value(m.detail_url, output_field=CharField())))
        n = n.union(*query_list).order_by('updated')
        return n


class NoteView(DetailView):
    """Реализация проверки на владение записью"""
    def get_object(self, queryset=None):
        o = super().get_object()
        if o.creator != self.request.user:
            raise Http404
        return o


class DetailFilmNote(NoteView):
    model = FilmNote


class DetailBookNote(NoteView):
    model = BookNote


class DetailTextNote(NoteView):
    model = TextNote


class DetailLinkNote(NoteView):
    model = LinkNote


class DetailCalendarNote(NoteView):
    model = CalendarNote


class DetailReflectionNote(NoteView):
    model = ReflectionNote
# End Notes block


# User Block
def profile(request):
    return render(request, 'registration/profile.html')


class RegistrationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class RegistrationUser(FormView):
    success_url = '/'
    form_class = RegistrationUserForm
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
# End User block


def index(request):
    return render(request, 'core/index.html')


class MoonNewsListView(ListView):
    paginate_by = 10
    model = MoonNews

    def get_queryset(self):
        return MoonNews.objects.annotate(short_content=Left('content', 300))\
            .values_list('title', 'published', 'short_content', 'publisher__username', 'tags', named=True)


def world_news(request):
    return redirect('core:moon_news')
