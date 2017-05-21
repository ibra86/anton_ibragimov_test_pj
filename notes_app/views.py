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
	# success_url=reverse('add_note')

	def form_valid(self, form):
		print 'validation'
		self.note = form.save(commit=False)
		self.note.published_date = timezone.now()
		self.note.save()
		if self.request.is_ajax():
			print 'was ajax_request'
			# return super(AddNote, self).form_valid(form)
			# response = super(AddNote, self).form_valid(form)
			# print response
			# return HttpResponseRedirect(self.get_success_url())
			# return redirect('add_note')
		else:
			print 'NO AJAX'
		# print self.note.pk
		return redirect('note_detail', pk=self.note.pk)

	# def form_invalid(self, form):
	# 	print 'no validation'
	# 	return super(AddNote, self).form_invalid(form)
	#
	# def get(self, request,*args,**kwargs):
	# 	print 'get_request'
	# 	return super(AddNote, self).get(request,*args,**kwargs)
	#
	# def post(self, request,*args,**kwargs):
	# 	print 'post_request'
	# 	return super(AddNote, self).post(request,*args,**kwargs)


    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm()
    # form = PostForm()
    # return render(request, 'post_edit.html', {'form':form})


