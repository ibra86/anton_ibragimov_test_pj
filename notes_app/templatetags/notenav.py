from django import template

register = template.Library()

@register.inclusion_tag('note_detail.html')
def notenav(note, note_num):
    return {'note': note, 'note_num': note_num}
