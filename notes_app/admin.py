from django.contrib import admin

# Register your models here.
from .models import Note
from .forms import NoteForm


class NoteAdmin(admin.ModelAdmin):
    form = NoteForm


admin.site.register(Note, NoteAdmin)
