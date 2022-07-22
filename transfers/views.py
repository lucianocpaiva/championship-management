from rest_framework import viewsets

from transfers.serializers import TransferSerializer
from transfers.models import Transfer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
