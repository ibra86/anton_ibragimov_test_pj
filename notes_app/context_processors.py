def notes_num(request):
	from .models import Note
	notes_num = len(Note.objects.all())
	return {'notes_num':notes_num}

def portal_url(request):
	PORTAL_URL = request.build_absolute_uri()
	return {'PORTAL_URL': PORTAL_URL[:-1]}