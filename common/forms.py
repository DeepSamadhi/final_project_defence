from django import forms


class SearchInLibraryForm(forms.Form):
    search = forms.TextInput()
