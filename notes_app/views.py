from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from .models import Note, RequestStat
from .forms import NoteForm
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect, render

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
            print "AJAX request"
        return redirect('note_detail', pk=self.note.pk)


class WidgetTemplate(TemplateView):
    template_name = 'widget_example.html'


def requests(request):
    requests = RequestStat.objects.all().order_by('-id')[:10]

    if request.is_ajax():
        new_req_num = len(RequestStat.objects.filter(is_new=True))
        req_stat = [str(k) for k in requests]
        RequestStat.objects.filter(is_new=True).update(is_new=False)
        return JsonResponse({'new_req_num': new_req_num, 'req_stat': req_stat})

    return render(request, 'requests.html', {'requests': requests})
