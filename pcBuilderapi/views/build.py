from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Build

class BuildView(ViewSet):
    def retrieve(self, request, pk):
        build = Build.objects.get(pk=pk)
        serializer = BuildSerializer(build)
        return Response(serializer.data)
        
    def list(self, request):
        builds = Build.objects.all()
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data)
    
class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'title', 'builder', 'img', 'price', 'rating')