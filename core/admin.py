from django.contrib import admin
from .models import FilmNote, CalendarNote, ReflectionNote, BookNote, TextNote, LinkNote
from .models import MoonNews, WorldNews, WorldNewsCategory
# Note registration
admin.site.register(FilmNote)
admin.site.register(CalendarNote)
admin.site.register(ReflectionNote)
admin.site.register(BookNote)
admin.site.register(TextNote)
admin.site.register(LinkNote)

# News registration
admin.site.register(MoonNews)
admin.site.register(WorldNews)
admin.site.register(WorldNewsCategory)
