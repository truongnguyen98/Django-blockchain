from rest_framework import serializers
from .models import Transaction, Block

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        transaction = Transaction
        fields = ['index','common_name'
        #,'date','region','country','company','company','other'
        ]

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['hash', 'previous_hash', 'data', 'time_stamp', 'index', 'nonce']

    # def as_json(self):
    #     self.is_valid()
    #     data = dict(self.validated_data)
    #     data['time_stamp'] = str(data['time_stamp'])
    #     return data

