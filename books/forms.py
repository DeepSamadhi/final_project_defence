from django import forms

from cloudinary.forms import CloudinaryFileField  

from .models import Books, Autors




class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books

        # image = CloudinaryFileField(
        #     attrs = { 'style': "margin-top: 30px" }, 
        #     options = { 
        #         'tags': "directly_uploaded",
        #         'crop': 'limit', 'width': 1000, 'height': 1000,
        #         'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
        #     })

        fields = ['title', 'description', 'image', 'genre', 'autor', 'publisher','year_of_publication'
        ]
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'image': 'Image:',
            'genre': 'Genre:',
            'autor': 'Author:',
            'publisher': 'Publisher:',
            'year_of_publication': 'Year Of Publication'
        }

        widgets = {
            'title': forms.TextInput(attrs= {'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Author'}),
            'publisher': forms.TextInput(attrs={'placeholder': 'Publisher'}),
            'year_of_publication': forms.NumberInput(attrs={'placeholder': 'Year Of Publication'}),
        }
        



class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'image', 'genre', 'autor', 'publisher','year_of_publication']

        labels = {
                'title': 'Title:',
                'description': 'Description:',
                'image': 'Image:',
                'genre': 'Genre:',
                'autor': 'Author:',
                'publisher': 'Publisher:',
                'year_of_publication': 'Year Of Publication'
            }
