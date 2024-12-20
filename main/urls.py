from collections import namedtuple

from django.urls import path

from . import ap_views
from main.api_generics import *
urlpatterns = [
    path('list/', ap_views.AccountListAPIView.as_view(), name='account_list'),
    path('detail/<uuid:guid>/', ap_views.AccountDetailAPView.as_view(), name='account_detail'),

    # Generics uchun
    path('generic-list/', AccountGenericListAPIView.as_view(), name='account_generics_list'),
    path('generic-create/', AccountListCreateAPIView.as_view(), name='account_generics_create'),
    path('generic-retrieve/<uuid:guid>/', AccountRetrieveAPIView.as_view(), name='account_retrieve'),
    path('generic-update/<uuid:guid>/', AccountUpdateAPIView.as_view(), name='account_update'),
    path('generic-destroy/<uuid:guid>/', AccountDestroyAPIView.as_view(), name='account_destroy'),
    path('generic-retrieve-update-destroy/<uuid:guid>/', AccountRetrieveUpdateDestroyAPIView.as_view(),
         name='account_rud'),
]
