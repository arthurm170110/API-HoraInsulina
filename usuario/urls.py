from django.urls import path
from rest_framework.routers import DefaultRouter

from refeicao.views import RefeicaoPorUsuarioViewSet
from checkin.views import RelatorioAnualView, RelatorioMensalView, CheckinPorUsuarioViewSet
from usuario.views import CadastrarListarUsuario, AlterarDeletarUsuario


router = DefaultRouter()
router.register(r'(?P<usuario_id>[^/.]+)/refeicao', RefeicaoPorUsuarioViewSet, basename='listagem_refeicao')
router.register(r'(?P<usuario_id>[^/.]+)/checkin', CheckinPorUsuarioViewSet, basename='listagem_checkin')
urlpatterns = [

    path('', CadastrarListarUsuario.as_view(), name='cadastro'),
    path('<int:id>/', AlterarDeletarUsuario.as_view(), name='altrar_deletar'),
    path('<int:usuario_id>/relatorioanual/', RelatorioAnualView.as_view(), name='relatorio_anual'),
    path('<int:usuario_id>/relatoriomensal/', RelatorioMensalView.as_view(), name='relatorio_mensal'),

]
urlpatterns += router.urls
