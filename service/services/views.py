# from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializer
from django.db.models import Prefetch


class SubscriptionView(ReadOnlyModelViewSet):
    # стандартный prefetch вытягивает все поля всех моделей
    # queryset = Subscription.objects.all().prefetch_related('client__user')
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user') \
                 .only('company_name', 'user__email'))
    )
    serializer_class = SubscriptionSerializer
