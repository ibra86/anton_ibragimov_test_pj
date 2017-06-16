from django.views.generic import ListView
from .models import Note

# Create your views here.


class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'
