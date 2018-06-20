from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=100)
	email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class' : 'form-control','style': 'height: 6em;'}))
	
class ContactForm(forms.Form):
	subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=200)
	email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class' : 'form-control'}))
	message = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class' : 'form-control','style': 'height: 6em;'}))
