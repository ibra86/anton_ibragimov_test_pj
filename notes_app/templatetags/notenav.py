from django import template

register = template.Library()


@register.inclusion_tag('note_detail.html')
def notenav(note):
    return {'note': note}
