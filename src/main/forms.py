from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=50, label="Your Surname", widget=forms.TextInput(attrs={'class': 'form-control'}))
#     number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
#     register_date = forms.DateTimeField()
#     age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label="Your Surname", widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        exclude = ("register_date",)



# class StudentForm2(forms.ModelForm):
#     first_name = forms.CharField(label="Your Name: ModelForm forms.py tarafından degistirildi")
#     last_name = forms.CharField(label="Surname: ModelForm forms.py tarafından degistirildi")

#     class Meta:
#         model = Student
#         # fields = ("first_name", "last_name")
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['first_name'].label = "Your Name: ModelForm forms.py __init__ tarafından degistirildi"