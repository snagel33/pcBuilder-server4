from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import BuildPart

class BuildPartView(ViewSet):
    def retrieve(self, request, pk):
        buildPart = BuildPart.objects.get(pk=pk)
        serializer = BuildPartSerializer(buildPart)
        return Response(serializer.data)
    
    def list(self, request):
        buildParts = BuildPart.objects.all()
        serializer = BuildPartSerializer(buildParts, many=True)
        return Response(serializer.data)
    
class BuildPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildPart
        fields = ('id', 'part', 'build')
        depth = 3