from django.forms import ModelForm
from .models import Transaction


class ProducerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','expire_date','country','amount','fileAttached']
class ShipperForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount','fileAttached']
class WholesalerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount','fileAttached']
class DetailerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount','fileAttached']
    

