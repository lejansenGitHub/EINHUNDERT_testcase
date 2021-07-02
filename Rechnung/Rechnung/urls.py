from django.urls import path, include

urlpatterns = [
    path('', include('invoice.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]