def notes_num(request):
    from .models import Note
    notes_num = len(Note.objects.all())
    return {'notes_num':notes_num}

def portal_url(request):
    if request.is_secure():
        secur_req = "https://"
    else:
        secur_req = "http://"
    PORTAL_URL = secur_req+request.get_host()#build_absolute_uri()
    return {'PORTAL_URL': PORTAL_URL}