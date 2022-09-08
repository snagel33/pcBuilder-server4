from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import PartType, partType

class PartTypeView(ViewSet):
    def retrieve(self, request, pk):
        partType = PartType.objects.get(pk=pk)
        serializer = PartTypeSerializer(partType)
        return Response(serializer.data)
        
    def list(self, request):
        partTypes = PartType.objects.all()
        serializer = PartTypeSerializer(partTypes, many=True)
        return Response(serializer.data)
    
class PartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartType
        fields = ('id', 'label')
        