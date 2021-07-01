from django.urls import path, include
from invoice.views import InvoiceViewSet, ContractViewSet, UserViewSet, api_root
from rest_framework import renderers

invoice_list = InvoiceViewSet.as_view({
    'get': 'list',
    'post': 'postCustom'
})

invoice_detail = InvoiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

contract_list = ContractViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

contract_detail = ContractViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    path('', api_root),
    path('invoice/', invoice_list, name='invoice-list'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('contract/', contract_list, name='contract-list'),
    path('contract/<int:pk>/', contract_detail, name='contract-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
]














# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from invoice import views
#
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'invoice', views.InvoiceViewSet)
# router.register(r'contract', views.ContractViewSet)
# router.register(r'users', views.UserViewSet)
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]