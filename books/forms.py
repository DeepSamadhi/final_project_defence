from django import forms


from .models import Books, Autors



class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'image', 'genre', 'autor', 'publisher','year_of_publication'
        # try:
        #     'year_of_publication'=int(request.POST['year_of_publication'])
        # except:
        #     raise ValueError("You must enter an INTEGER")
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