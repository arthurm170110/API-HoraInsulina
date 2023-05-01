from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Refeicao

from .serializers import RefeicaoSerializer


    
class RefeicaoViewSet(viewsets.ModelViewSet):
    queryset = Refeicao.objects.all()
    serializer_class = RefeicaoSerializer
    # permission_classes = (IsAuthenticated, )

class RefeicaoPorUsuarioViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = RefeicaoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']

        return Refeicao.objects.filter(usuario=usuario_id)
