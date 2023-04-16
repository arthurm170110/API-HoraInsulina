from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Refeicao

from .serializers import RefeicaoSerializer


    
class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['alarme']


class RefeicaoPorUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = RefeicaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    filterset_fields = ['alarme']

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']

        return Refeicao.objects.filter(usuario=usuario_id)
