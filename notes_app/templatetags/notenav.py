from django import template

register = template.Library()


@register.inclusion_tag('note_detail.html')
def notenav(note, notes_num):
    return {'note': note, 'notes_num': notes_num}
