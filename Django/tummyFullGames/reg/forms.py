from django import forms

from .models import tribute

class PostForm(forms.ModelForm):

	class Meta:
		model = tribute
		fields = ('name', 'skill', 'district', 'text',)