from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView

from .views import index, world_news, MoonNewsListView, NotesListView, profile,\
    DetailTextNote, DetailLinkNote, DetailBookNote, DetailFilmNote, DetailReflectionNote, DetailCalendarNote,\
    TextNoteAdd, RegistrationUser, FilmNoteAdd, BookNoteAdd, CalendarNoteAdd, ReflectionNoteAdd, LinkNoteAdd,\
    TextNoteChange, LinkNoteChange, FilmNoteChange, BookNoteChange, ReflectionNoteChange, CalendarNoteChange,\
    TextNoteDelete, LinkNoteDelete, FilmNoteDelete, BookNoteDelete, ReflectionNoteDelete, CalendarNoteDelete

app_name = 'core'

# todo change namespace to notes
notes_patterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('detail/text_note/<int:pk>/', DetailTextNote.as_view(), name='textnote_detail'),
    path('detail/link_note/<int:pk>/', DetailLinkNote.as_view(), name='linknote_detail'),
    path('detail/book_note/<int:pk>/', DetailBookNote.as_view(), name='booknote_detail'),
    path('detail/film_note/<int:pk>/', DetailFilmNote.as_view(), name='filmnote_detail'),
    path('detail/reflection_note/<int:pk>/', DetailReflectionNote.as_view(), name='reflectionnote_detail'),
    path('detail/calendar_note/<int:pk>/', DetailCalendarNote.as_view(), name='calendarnote_detail'),
    path('create/text_note/', TextNoteAdd.as_view(), name='textnote_create'),
    path('create/film_note/', FilmNoteAdd.as_view(), name='filmnote_create'),
    path('create/book_note/', BookNoteAdd.as_view(), name='booknote_create'),
    path('create/calendar_note/', CalendarNoteAdd.as_view(), name='calendarnote_create'),
    path('create/reflection_note/', ReflectionNoteAdd.as_view(), name='reflectionnote_create'),
    path('create/link_note/', LinkNoteAdd.as_view(), name='linknote_create'),
    path('change/text_note/<int:pk>/', TextNoteChange.as_view(), name='textnote_change'),
    path('change/link_note/<int:pk>/', LinkNoteChange.as_view(), name='linknote_change'),
    path('change/film_note/<int:pk>/', FilmNoteChange.as_view(), name='filmnote_change'),
    path('change/book_note/<int:pk>/', BookNoteChange.as_view(), name='booknote_change'),
    path('change/reflection_note/<int:pk>/', ReflectionNoteChange.as_view(), name='reflectionnote_change'),
    path('change/calendar_note/<int:pk>/', CalendarNoteChange.as_view(), name='calendarnote_change'),
    path('delete/text_note/<int:pk>/', TextNoteDelete.as_view(), name='textnote_delete'),
    path('delete/link_note/<int:pk>/', LinkNoteDelete.as_view(), name='linknote_delete'),
    path('delete/film_note/<int:pk>/', FilmNoteDelete.as_view(), name='filmnote_delete'),
    path('delete/book_note/<int:pk>/', BookNoteDelete.as_view(), name='booknote_delete'),
    path('delete/reflection_note/<int:pk>/', ReflectionNoteDelete.as_view(), name='reflectionnote_delete'),
    path('delete/calendar_note/<int:pk>/', CalendarNoteDelete.as_view(), name='calendarnote_delete'),
]
# change namespace to account
account_patterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('loout/', LogoutView.as_view(), name='logout'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('registration/', RegistrationUser.as_view(), name='registration')
]

urlpatterns = [
    path('', index, name='index'),
    path('moon_news/', MoonNewsListView.as_view(), name='moon_news'),
    path('world_news/', world_news, name='world_news'),
    path('notes/', include(notes_patterns)),
    path('account/', include(account_patterns))
]
