from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import Usuario

from .serializers import UsuarioSerializer



class CadastrarListarUsuario(APIView):

    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlterarDeletarUsuario(APIView):

    permission_classes = (IsAuthenticated, )

    def get_object(self, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            raise NotFound()

    def get(self, request, id):
        usuario = self.get_object(id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, id):
        usuario = self.get_object(id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.update(usuario, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        usuario = self.get_object(id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
