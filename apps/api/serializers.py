from django.contrib.auth.models import User
from rest_framework import serializers
from apps.core.models import Taxi


class UserSerializer(serializers.HyperlinkedModelSerializer):
    taxis = serializers.HyperlinkedRelatedField(many=True, view_name='taxi-detail', queryset=Taxi.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'taxis')


class TaxiSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    color_name = serializers.ReadOnlyField(source='get_color_display')
    calificacion_name = serializers.ReadOnlyField(source='get_calificacion_display')
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        formato = obj.created.strftime("%A %d. %B %Y %I:%M%p")
        return formato

    class Meta:
        model = Taxi
        fields = ('numero', 'comentario', 'usuario', 'calificacion', 'calificacion_name', 'created', 'costo', 'color',
                  'color_name')


class TaxiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxi
        fields = '__all__'
