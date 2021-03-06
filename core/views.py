from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Value, CharField
from django.db.models.functions import Left
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from core.forms import TextNoteForm, FilmNoteForm, BookNoteForm, ReflectionNoteForm, CalendarNoteForm, LinkNoteForm, \
    MoonNewsForm
from core.models import MoonNews
from core.models import TextNote, BookNote, LinkNote, FilmNote, ReflectionNote, CalendarNote, AVAILABLE_NOTES
from django.contrib.auth.forms import UserCreationForm

# todo template for change password
# todo reset password
# todo registration
# todo шаблон для формы с наследованием управлением выводом


# Note block
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
    template_name = 'core/notes.html'
    notes = {  # возможно это стоит вынести в глобальное пространство
        'text': TextNote,
        'link': LinkNote,
        'book': BookNote,
        'film': FilmNote,
        'reflection': ReflectionNote,
        'calendar': CalendarNote,
    }

    def get_queryset(self):
        u = self.request.user
        notetype = self.request.GET.get('notetype')
        if notetype:
            notemodel = self.notes[notetype]
            queryset = notemodel.objects.filter(creator=u).\
                annotate(type_name=Value(AVAILABLE_NOTES[0].type_name, output_field=CharField())
                         , detail_url=Value(AVAILABLE_NOTES[0].detail_url, output_field=CharField())).\
                values_list('id', 'title', 'type_name', 'detail_url', 'created', 'updated', 'tags', named=True)
        else:
            queryset = AVAILABLE_NOTES[0].objects\
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
            queryset = queryset.union(*query_list).order_by('updated')
        return queryset


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


# News block
class MoonNewsListView(ListView):
    paginate_by = 10
    model = MoonNews

    def get_queryset(self):
        return MoonNews.objects.only('title', 'published', 'content', 'publisher__username', 'tags')\
            .annotate(short_content=Left('content', 300))


class MoonNewsAdd(PermissionRequiredMixin, FormView):
    permission_required = 'core.add_moonnews'
    success_url = reverse_lazy('core:moonnews-view')
    form_class = MoonNewsForm
    template_name = 'core/moonnews_form.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.publisher = self.request.user
        news.save()
        return super().form_valid(form)


class MoonNewsDetail(DetailView):
    model = MoonNews


class MoonNewsChange(PermissionRequiredMixin, UpdateView):
    permission_required = 'core.change_moonnews'
    model = MoonNews
    succes_url = reverse_lazy('core:moonnews-view')
    form_class = MoonNewsForm


class MoonNewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'core.delete_moonnews'
    success_url = reverse_lazy('core:moonnews-view')
    model = MoonNews
    template_name = 'core/moonnews_delete.html'


def world_news(request):
    return redirect('core:moonnews-view')
# End News block
