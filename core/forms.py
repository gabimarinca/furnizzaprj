from django import forms
from core.models import Review

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Write review"})) 

    class Meta:
        model = Review
        fields = ['comment', 'rating']