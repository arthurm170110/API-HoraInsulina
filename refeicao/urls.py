from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.RefeicaoViewSet, basename='refeicao')
urlpatterns = router.urls
