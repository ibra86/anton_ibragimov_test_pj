from django.views.generic import ListView, DetailView
from .models import Note

# Create your views here.


class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'


class NoteDetail(DetailView):
    model = Note
    template_name = 'note_detail_tagged.html'
    context_object_name = 'note'
