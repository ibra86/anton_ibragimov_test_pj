from django import forms
from .models import Note


class UppercaseCharField(forms.CharField):
    def to_python(self, value):
        return value.upper()


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), min_length=10)

    class Meta:
        model = Note
        fields = ["title", "text"]
