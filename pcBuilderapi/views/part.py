from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Part, PartType

class PartView(ViewSet):
    def retrieve(self, request, pk):
        part = Part.objects.get(pk=pk)
        serializer = PartSerializer(part)
        return Response(serializer.data)
    
    def list(self, request):
        parts = Part.objects.all()
        partType = request.query_params.get('type', None)
        if partType is not None:
            parts = parts.filter(partType_id=partType)
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        partType = PartType.objects.get(pk=request.data["partTypeId"])
        
        part = Part.objects.create(
            partType=partType,
            maker=request.data["maker"],
            name=request.data["name"],
            img=request.data["img"],
            description=request.data["description"],
            price=request.data["price"]
        )
        serializer = PartSerializer(part)
        return Response(serializer.data)

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'maker', 'name', 'img', 'description', 'price', 'partType_id')
        depth = 1