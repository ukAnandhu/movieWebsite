from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self,*args,**kwargs):
        super(MovieForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['poster'].widget.attrs['placeholder'] = 'Enter poster'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter descrption'
        self.fields['release_date'].widget.attrs['placeholder'] = 'Enter release date'
        self.fields['actors'].widget.attrs['placeholder'] = 'Enter actors names'
        self.fields['category'].widget.attrs['placeholder'] = 'Enter category'
        self.fields['trailer_link'].widget.attrs['placeholder'] = 'Enter trailer link'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']
    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)
        self.fields['review'].widget.attrs['placeholder'] = 'Enter Review'
        self.fields['rating'].widget.attrs['placeholder'] = 'Enter rating'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

