from rest_framework import status
from rest_framework import generics, permissions, renderers, viewsets
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from invoice.models import Invoice, Contract
from invoice.serializers import UserSerializer, InvoiceSerializer, ContractSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'invoice': reverse('invoice-list', request=request, format=format),
        'contract': reverse('contract-list', request=request, format=format),
    })
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]



class ContractViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    
    
    def put(self, request, *args, **kwargs):
        contract = self.get_object()
        data = request.data
        
        contract.contract_label = data["contract_label"]
        contract.contract_number = data["contract_number"]
        
        
        contract.save()
        
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        contract = self.objects.get()
        data = request.data


        
        contract.contract_label = data.get("contract_label", contract.contract_label)
        contract.contract_number = data.get("contract_number", contract.contract_number)

        contract.save()
        serializer = ContractSerializer(contract)

        return Response(serializer.data)
    

        
        
class InvoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'billed':['lt'],
                        #'billed':['gte', 'lte', 'exact', 'gt', 'lt'],
                        'creation_date':['exact'],
                        'contract':['exact']}
    
    def postCustom(self , request):

        serializer = InvoiceSerializer(data = request.data)
        postIsValid = True
        errorMsg = "ERROR:"
        
        data = request.data
        print("invoice_number: ", data["invoice_number"])
        if(data["invoice_number"].isdigit() == False):
            postIsValid = False
            errorMsg = errorMsg + "invoice_number needs to be integer"
        if serializer.is_valid() and postIsValid:
            serializer.save()
            return Response({"status" : "Success"} , status = status.HTTP_201_CREATED)
        else:
            return Response({"status" : errorMsg} , status = status.HTTP_400_BAD_REQUEST)
            
    
    def put(self, request, *args, **kwargs):
        invoice = self.get_object()
        data = request.data
        
        invoice.invoice_number = data["invoice_number"]
        invoice.file_name = data["file_name"]
        invoice.creation_date = data["creation_date"]
        invoice.payment_target_date = data["payment_target_date"]
        invoice.cancellation_date = data["cancellation_date"]
        invoice.period_start = data["period_start"]
        invoice.period_end = data["period_end"]
        invoice.counter_start = data["counter_start"]
        invoice.counter_end = data["counter_end"]
        invoice.net_sum = data["net_sum"]
        invoice.billed = data["billed"]
        invoice.contract = data["contract"]
        invoice.invoice_update = data["invoice_update"]
        invoice.draft = data["draft"]
        
        
        invoice.save()
        
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        invoice = self.objects.get()
        data = request.data


        
        invoice.invoice_number = data.get("invoice_number", invoice.invoice_number)
        invoice.file_name = data.get("file_name", invoice.file_name)
        invoice.creation_date = data.get("creation_date", invoice.creation_date)
        invoice.payment_target_date = data.get("payment_target_date", invoice.payment_target_date)
        invoice.cancellation_date = data.get("cancellation_date", invoice.cancellation_date)
        invoice.period_start = data.get("period_start", invoice.period_start)
        invoice.period_end = data.get("period_end", invoice.period_end)
        invoice.counter_start = data.get("counter_start", invoice.counter_start)
        invoice.counter_end = data.get("counter_end", invoice.counter_end)
        invoice.net_sum = data.get("net_sum", invoice.net_sum)
        invoice.billed = data.get("billed", invoice.billed)
        invoice.contract = data.get("contract", invoice.contract)
        invoice.invoice_update = data.get("invoice_update", invoice.invoice_update)
        invoice.draft = data.get("draft", invoice.draft)

        invoice.save()
        serializer = InvoiceSerializer(invoice)

        return Response(serializer.data)
    

        
        