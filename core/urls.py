from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import index, world_news, MoonNewsListView, NotesListView, \
    profile, RegistrationUser, \
    DetailTextNote, DetailLinkNote, DetailBookNote, DetailFilmNote, DetailReflectionNote, DetailCalendarNote, \
    TextNoteAdd, FilmNoteAdd, BookNoteAdd, CalendarNoteAdd, ReflectionNoteAdd, LinkNoteAdd, \
    TextNoteChange, LinkNoteChange, FilmNoteChange, BookNoteChange, ReflectionNoteChange, CalendarNoteChange, \
    TextNoteDelete, LinkNoteDelete, FilmNoteDelete, BookNoteDelete, ReflectionNoteDelete, CalendarNoteDelete, \
    MoonNewsDetail, MoonNewsAdd, MoonNewsChange, MoonNewsDelete

app_name = 'core'

# todo change namespace to notes
notes_patterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('detail/text_note/<int:pk>/', DetailTextNote.as_view(), name='textnote-detail'),
    path('detail/link_note/<int:pk>/', DetailLinkNote.as_view(), name='linknote-detail'),
    path('detail/book_note/<int:pk>/', DetailBookNote.as_view(), name='booknote-detail'),
    path('detail/film_note/<int:pk>/', DetailFilmNote.as_view(), name='filmnote-detail'),
    path('detail/reflection_note/<int:pk>/', DetailReflectionNote.as_view(), name='reflectionnote-detail'),
    path('detail/calendar_note/<int:pk>/', DetailCalendarNote.as_view(), name='calendarnote-detail'),
    path('create/text_note/', TextNoteAdd.as_view(), name='textnote-create'),
    path('create/film_note/', FilmNoteAdd.as_view(), name='filmnote-create'),
    path('create/book_note/', BookNoteAdd.as_view(), name='booknote-create'),
    path('create/calendar_note/', CalendarNoteAdd.as_view(), name='calendarnote-create'),
    path('create/reflection_note/', ReflectionNoteAdd.as_view(), name='reflectionnote-create'),
    path('create/link_note/', LinkNoteAdd.as_view(), name='linknote-create'),
    path('change/text_note/<int:pk>/', TextNoteChange.as_view(), name='textnote-change'),
    path('change/link_note/<int:pk>/', LinkNoteChange.as_view(), name='linknote-change'),
    path('change/film_note/<int:pk>/', FilmNoteChange.as_view(), name='filmnote-change'),
    path('change/book_note/<int:pk>/', BookNoteChange.as_view(), name='booknote-change'),
    path('change/reflection_note/<int:pk>/', ReflectionNoteChange.as_view(), name='reflectionnote-change'),
    path('change/calendar_note/<int:pk>/', CalendarNoteChange.as_view(), name='calendarnote-change'),
    path('delete/text_note/<int:pk>/', TextNoteDelete.as_view(), name='textnote-delete'),
    path('delete/link_note/<int:pk>/', LinkNoteDelete.as_view(), name='linknote-delete'),
    path('delete/film_note/<int:pk>/', FilmNoteDelete.as_view(), name='filmnote-delete'),
    path('delete/book_note/<int:pk>/', BookNoteDelete.as_view(), name='booknote-delete'),
    path('delete/reflection_note/<int:pk>/', ReflectionNoteDelete.as_view(), name='reflectionnote-delete'),
    path('delete/calendar_note/<int:pk>/', CalendarNoteDelete.as_view(), name='calendarnote-delete'),
]
# change namespace to account
account_patterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('loout/', LogoutView.as_view(), name='logout'),
    path('change_password/', PasswordChangeView.as_view(), name='change_password'),
    path('registration/', RegistrationUser.as_view(), name='registration')
]
# change namespace to news
news_patterns = [
    path('moon/', MoonNewsListView.as_view(), name='moonnews-view'),
    path('moon/add/', MoonNewsAdd.as_view(), name='moonnews-add'),
    path('moon/detail/<int:pk>/', MoonNewsDetail.as_view(), name='moonnews-detail'),
    path('moon/change/<int:pk>/', MoonNewsChange.as_view(), name='moonnews-change'),
    path('moon/delete/<int:pk>/', MoonNewsDelete.as_view(), name='moonnews-delete'),
    path('world/', world_news, name='worldnews'),
]


urlpatterns = [
    path('', index, name='index'),
    path('news/', include(news_patterns)),
    path('notes/', include(notes_patterns)),
    path('account/', include(account_patterns))
]
