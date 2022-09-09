from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Builder

class BuilderView(ViewSet):
    def retrieve(self, request, pk):
        builder = Builder.objects.get(pk=pk)
        serializer = BuilderSerializer(builder)
        return Response(serializer.data)
        
    def list(self, request):
        builders = Builder.objects.all()
        serializer = BuilderSerializer(builders, many=True)
        return Response(serializer.data)
    
class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        fields = ('id', 'user', 'userName', 'bio', 'img')