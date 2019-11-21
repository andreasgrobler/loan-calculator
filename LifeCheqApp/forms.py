from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Input


class InputForm(forms.ModelForm):
    name_of_loan = forms.CharField(
        label='Name of the loan:',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    
    price = forms.FloatField(
        label='Enter the purchase price of the property',
        help_text='Do not leave spaces between values and use a decimal point.',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    
    deposit = forms.FloatField(
        label='Enter the deposit that will be paid on the property',
        help_text='Do not leave spaces between values and use a decimal point.',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    
    interest_rate = forms.FloatField(
        label='Enter the annual interest rate of the loan',
        help_text='Do not indicate this value as a percentage.',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    
    term = forms.FloatField(
        label='Enter the term of the loan in years',
        widget=forms.TextInput(attrs={'placeholder': ''})
    )

    # def __init__(self, *args, **kwargs):
    #     super(InputForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)      

    class Meta:
        model = Input
        fields = ['name_of_loan','price', 'deposit', 'interest_rate', 'term']

