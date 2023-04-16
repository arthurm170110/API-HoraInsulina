from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Checkin

from .serializers import CheckinSerializer


class CadastrarListarCheckin(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer


class CheckinPorUsuarioViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = (IsAuthenticated, )
    
    serializer_class = CheckinSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']

        return Checkin.objects.filter(usuario=usuario_id)
    


class RelatorioAnualView(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, usuario_id):
        
        checkin = Checkin.objects.filter(usuario_id=usuario_id)
        relatorio_anual = {}

        for elementos in checkin:
            ano = elementos.data.strftime("%Y")

            if ano in relatorio_anual:
                relatorio_anual[ano][0] += elementos.glicose
                relatorio_anual[ano][1] += 1
            else:
                relatorio_anual[ano] = [elementos.glicose, 1]
        
        for chave in relatorio_anual.keys():
            media = round(relatorio_anual[chave][0] / relatorio_anual[chave][1], 2)
            relatorio_anual[chave].append(media)
            
        return Response(relatorio_anual)

class RelatorioMensalView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, usuario_id):
        
        checkin = Checkin.objects.filter(usuario_id=usuario_id)
        relatorio_mensal = {}

        for elementos in checkin:
            ano_mes = elementos.data.strftime("%Y-%m")

            if ano_mes in relatorio_mensal:
                relatorio_mensal[ano_mes][0] += elementos.glicose
                relatorio_mensal[ano_mes][1] += 1
            else:
                relatorio_mensal[ano_mes] = [elementos.glicose, 1]
        
        for chave in relatorio_mensal.keys():
            media = round(relatorio_mensal[chave][0] / relatorio_mensal[chave][1], 2)
            relatorio_mensal[chave].append(media)
            
        return Response(relatorio_mensal)
