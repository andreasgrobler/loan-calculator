from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Input


class InputForm(forms.ModelForm):
    name_of_loan = forms.CharField(
        label='Provide a name for the loan:',
        widget=forms.TextInput(attrs={'placeholder': 'Home Loan'})
    )
    
    price = forms.FloatField(
        label='Please enter the purchase price of the property',
        help_text='Do not leave spaces between values and use a decimal point.',
        widget=forms.TextInput(attrs={'placeholder': '1000000'})
    )
    
    deposit = forms.FloatField(
        label='Please enter the deposit that will be paid on the property',
        help_text='Do not leave spaces between values and use a decimal point.',
        widget=forms.TextInput(attrs={'placeholder': '200000'})
    )
    
    interest_rate = forms.FloatField(
        label='Enter the annual interest rate of the loan',
        help_text='Do not indicate this value as a percentage.',
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
        model = Input
        fields = ['name_of_loan','price', 'deposit', 'interest_rate', 'term']

