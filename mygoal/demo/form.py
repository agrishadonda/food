from django import forms
from . import models
# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]
class date(forms.ModelForm):
    class Meta:
        model = models.datemodel
        fields = '__all__'
        widgets = {
                    'dates': forms.DateInput(attrs={
                    'placeholder': 'Date',
                    'class':"date"})
                } 
        
    
class email(forms.ModelForm):           
    class Meta:
        model = models.TestModel
        fields = '__all__'
        # labels = {
        #                 'email': '',
        #             }
        widgets = {
                    'email': forms.EmailInput(attrs={'placeholder': 'Your Email'})
                }                 
                                        

class HotelForm(forms.ModelForm):
    class Meta:
        model = models.StudentProfile
        fields = ['fname','lname','date']
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Firstname*'
                }),
            
             'lname': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Lastname*'
                }),
             
              'date': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'email*'
                }),
             
        }
        
Country_Choices = [
    ('country1','India'),
    ('country2','USA'),
    ('country3','UK')
]
        
class MyForm(forms.Form):
    name = forms.CharField(label = 'Name',max_length=7,required=True)
    age = forms.IntegerField(label = 'Age',required=True)
    city = forms.CharField(label = 'City',required=True)
    country = forms.CharField(label='what is your country?',
                              widget = forms.Select(choices=Country_Choices))
    
PERSON_CHOICE = [
    ('persons1','person'),
    ('persons2','person2'),
    ('persons3','person3'),
    ('persons4','person4')
]
    
class PersonForm(forms.Form):
    person = forms.CharField(widget=forms.Select(choices=PERSON_CHOICE, attrs={"class":"per"}))