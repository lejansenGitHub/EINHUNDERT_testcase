from rest_framework import serializers
from invoice.models import Invoice, Contract

from django.contrib.auth.models import User


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contract
        fields = ['url', 'id', 'contract_label', 'contract_number']
        
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Invoice
        fields = ['url', 'id', 'invoice_number', 'file_name',  
                  'creation_date','payment_target_date', 'cancellation_date', 'period_start', 'period_end', 
                   'counter_start', 'counter_end', 'net_sum', 'billed', 'contract', 'invoice_update', 'draft']

        
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']