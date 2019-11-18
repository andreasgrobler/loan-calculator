from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from .models import InModel


class InForm(forms.ModelForm):
    name_of_loan = forms.CharField(
        label='Provide a title for the loan:',
        widget=forms.TextInput(attrs={'placeholder': 'Home Loan'})
    )
    
    price = forms.FloatField(
        label='Please enter the purchase price of the property',
        widget=forms.TextInput(attrs={'placeholder': '10000000'})
    )
    
    deposit = forms.FloatField(
        label='Please enter the deposit that will be paid on the property',
        widget=forms.TextInput(attrs={'placeholder': '2000000'})
    )
    
    interest_rate = forms.FloatField(
        label='Enter the annual interest rate of the loan (eg. 10 for 10%)',
        widget=forms.TextInput(attrs={'placeholder': '10.25'})
    )
    
    term = forms.FloatField(
        label='Enter the term of the loan in years',
        widget=forms.TextInput(attrs={'placeholder': '20'})
    )

    # def __init__(self, *args, **kwargs):
    #     super(InputForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)      

    class Meta:
        model = InModel
        fields = ['name_of_loan','price', 'deposit', 'interest_rate', 'term']

