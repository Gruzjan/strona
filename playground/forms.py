from django import forms

class NewClassForm(forms.Form):
    class_name = forms.CharField(label='Class id')