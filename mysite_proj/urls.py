from django.conf.urls import url
from django.contrib import admin
from notes_app.views import NoteList, NoteDetail, AddNote

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', NoteList.as_view(), name="home"),
	url(r'^note/(?P<pk>[0-9]+)/$', NoteDetail.as_view(), name='note_detail'),
    url(r'^note/add/$', AddNote.as_view(), name='add_note'),
]
