from rest_framework import status
from rest_framework import generics, permissions, renderers, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

from invoice.models import Invoice, Contract
from invoice.serializers import UserSerializer, InvoiceSerializer, ContractSerializer

import datetime
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
    
        
        
class InvoiceViewSetList(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'billed':['lte','gt'],
                        #'billed':['gte', 'lte', 'exact', 'gt', 'lt'],
                        'creation_date':['exact'],
                        'contract':['exact']}
    
    def postCustom(self , request):
        #ToDo: plausibility check for all inputs
        serializer = InvoiceSerializer(data = request.data)
        postIsValid = True
        errorMsg = "ERROR: "
        
        data = request.data
        print("invoice_number: ", data["invoice_number"])
        
        if(data["invoice_number"].isdigit() == False):
            postIsValid = False
            errorMsg = errorMsg + " :: " + "invoice_number needs to be integer"
        defaultInvoice = Invoice()
        try:
            period_start_input = datetime.datetime.strptime(data["period_start"], '%Y-%m-%d').date()
        except:
            period_start_input = defaultInvoice.period_start
        try:
            period_end_input = datetime.datetime.strptime(data["period_end"], '%Y-%m-%d').date()
        except:
            period_end_input = defaultInvoice.period_end
            
        if(period_start_input >= period_end_input):
            postIsValid = False
            errorMsg = errorMsg + " :: " + "period_end needs to be bigger than period_start"
            
        if serializer.is_valid() and postIsValid:
            serializer.save()
            return Response({"status" : "Success"} , status = status.HTTP_201_CREATED)
        else:
            return Response({"status" : errorMsg} , status = status.HTTP_400_BAD_REQUEST)
            
class InvoiceViewSetDetail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    #ToDo: implement patchCustom with plausibility check
    
    
    
    
    
    

        
        