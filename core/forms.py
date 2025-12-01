from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MediaContent

class SignUpForm(UserCreationForm):
    pass

class MediaContentForm(forms.ModelForm):
    # Override file field to accept the public_id string from the widget
    file = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = MediaContent
        fields = ['title', 'description', 'file', 'is_ai_generated']

    def clean_file(self):
        file_data = self.cleaned_data.get('file')
        if not file_data:
            raise forms.ValidationError("Please upload a file.")
        return file_data
