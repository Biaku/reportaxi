from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, status, mixins, generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route

from apps.api.permissions import IsOwnerOrReadOnly
from apps.api.serializers import TaxiSerializer, UserSerializer
from apps.core.models import Taxi


# -------------------------------------------------------------------------------------------------------
# |
# |         Ejemplo de vistas basadas en funcion para  la api de rest_framework
# |
# -------------------------------------------------------------------------------------------------------
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'taxis': reverse('taxi-list', request=request, format=format)
    })


@api_view(['GET', 'POST'])
def taxi_list(request):
    if request.method == 'GET':
        taxis = Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaxiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def taxi_detail(request, pk):
    """
    Retrieve, update or delete a taxi instance.
    """
    try:
        taxi = Taxi.objects.get(pk=pk)
    except Taxi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaxiSerializer(taxi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------------------------------------------------
# |
# |         Ejemplo de vistas basadas en clase (ApiView) para  la api de rest_framework
# |
# -------------------------------------------------------------------------------------------------------

class TaxiList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        taxis = Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaxiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxiDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Taxi.objects.get(pk=pk)
        except Taxi.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        taxi = self.get_object(pk)
        serializer = TaxiSerializer(taxi)
        return Response(serializer.data)

    def put(self, request, pk):
        taxi = self.get_object(pk)
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        taxi = self.get_object(pk)
        taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------------------------------------------------
# |
# |         Ejemplo de vistas basadas en clase usando mixins para  la api de rest_framework
# |
# -------------------------------------------------------------------------------------------------------

class TaxiListMixin(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaxiDetailMixin(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# -------------------------------------------------------------------------------------------------------
# |
# |         Ejemplo de vistas basadas en clase genericas para  la api de rest_framework
# |
# -------------------------------------------------------------------------------------------------------

class TaxiListGeneric(generics.ListCreateAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)  # permisos para solo lectura

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class TaxiDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)  # permisos para solo lectura


# -------------------------------------------------------------------------------------------------------
# |
# |         Ejemplo de vistas basadas en viewsets
# |
# -------------------------------------------------------------------------------------------------------
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaxiViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# -------------------------------------------------------------------------------------------------------
# |
# |         Vistas para el usuario
# |
# -------------------------------------------------------------------------------------------------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def search_taxi(request):
    if request.GET.get('numero'):
        print(request.GET['numero'])
        taxis = Taxi.objects.filter(numero=request.GET['numero'])
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data)
    else:
        return Response({'Por favor ingresa un numero correcto'}, status=status.HTTP_400_BAD_REQUEST)


class TaxiAppList(generics.ListAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
