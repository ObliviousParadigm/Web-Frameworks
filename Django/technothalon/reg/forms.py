from django import forms

from .models import team

class PostForm(forms.ModelForm):

	class Meta:
		model = team
		fields = ('name', 'uni', 'number_of_members', 'boarding')