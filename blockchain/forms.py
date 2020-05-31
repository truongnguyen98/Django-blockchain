from django import forms


class TransactionForm(forms.Form):
    index = forms.IntegerField()
    common_name= forms.CharField()
    #date = forms.DateField()
    #region = forms.CharField()
    #country = forms.CharField()
    #company = forms.CharField()
    #amount = forms.CharField()
    #file = forms.FileField()

