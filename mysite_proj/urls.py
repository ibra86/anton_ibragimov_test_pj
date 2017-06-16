from django.conf.urls import url
from django.contrib import admin
from notes_app.views import NoteList

from .settings import STATIC_URL
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', NoteList.as_view(), name="home"),
] + static(STATIC_URL, document_root=settings.STATIC_ROOT)
