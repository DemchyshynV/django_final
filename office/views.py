from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

from .serializers import OfficeSerializer
from .models import OfficeModel


class OfficeView(CreateAPIView, ListModelMixin):
    serializer_class = OfficeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        id = params.get('id', None)
        if not id:
            return OfficeModel.objects.all()
        return OfficeModel.objects.filter(id=id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
