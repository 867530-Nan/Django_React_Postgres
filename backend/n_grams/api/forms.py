from django import forms
from n_grams.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')
