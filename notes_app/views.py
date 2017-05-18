from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
class NoteList(ListView):
	model = Note
	template_name = 'note_list.html'
	context_object_name = 'notes'

class NoteDetail(DetailView):
	model = Note
	template_name = 'note_detail_tagged.html'
	context_object_name = 'note'
