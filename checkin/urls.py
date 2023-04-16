from django.urls import path

from checkin.views import CadastrarListarCheckin


urlpatterns = [

    path('', CadastrarListarCheckin.as_view(), name='cadastro'),

]
