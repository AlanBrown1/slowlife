from django import forms

class ImageUploadForm(forms.Form):
	image = forms.ImageField()

class FileUploadForm(forms.Form):
	file = forms.FileField()