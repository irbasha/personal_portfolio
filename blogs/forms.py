from django import forms

class CommentForm(forms.Form):
	author = forms.CharField(max_length=100, widget=forms.TextInput())
	body = forms.CharField(widget=forms.Textarea())
