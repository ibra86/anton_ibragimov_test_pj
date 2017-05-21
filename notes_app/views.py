from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Note
from .forms import NoteForm
from django.utils import timezone

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

# Create your views here.
class NoteList(ListView):
	model = Note
	template_name = 'note_list.html'
	context_object_name = 'notes'

class NoteDetail(DetailView):
	model = Note
	template_name = 'note_detail_tagged.html'
	context_object_name = 'note'

class AddNote(CreateView):
	form_class = NoteForm
	template_name = 'add_note.html'

	def form_valid(self, form):
		self.note = form.save(commit=False)
		self.note.published_date = timezone.now()
		self.note.save()
		if self.request.is_ajax():
			pass
		return redirect('note_detail', pk=self.note.pk)


