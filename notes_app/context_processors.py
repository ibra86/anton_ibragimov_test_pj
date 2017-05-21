def notes_num(request):
    from .models import Note
    notes_num = len(Note.objects.all())
    return {'notes_num':notes_num}
