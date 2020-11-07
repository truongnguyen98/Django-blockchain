from django.forms import ModelForm
from .models import Transaction
from web3 import Web3
from multiform import MultiForm



class ProducerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','expire_date','country','amount']        

class ShipperForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount']

class WholesalerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount']
   
class DetailerForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['product_id','common_name','country','amount']

class LinksMultiForm(MultiForm):
    base_forms = {
        'producer': ProducerForm,
        'shipper': ShipperForm,
        'wholesaler': WholesalerForm,
        'detailer': DetailerForm,
    }
    



