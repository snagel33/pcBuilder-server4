from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Part

class PartView(ViewSet):
    def retrieve(self, request, pk):
        part = Part.objects.get(pk=pk)
        serializer = PartSerializer(part)
        return Response(serializer.data)
    
    def list(self, request):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'maker', 'name', 'img', 'description', 'price', 'partType_id')