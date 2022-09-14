from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Build, Builder, builder
from django.core.exceptions import ValidationError

class BuildView(ViewSet):
    def retrieve(self, request, pk):
        build = Build.objects.get(pk=pk)
        serializer = BuildSerializer(build)
        return Response(serializer.data)
        
    def list(self, request):
        builds = Build.objects.all()
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        builder = Builder.objects.get(user=request.auth.user)
                
        build = Build.objects.create(
            title=request.data["title"],
            builder=builder,
            img=request.data["img"],
            price=request.data["price"],
            rating=request.data["rating"]
        )
        serializer = BuildSerializer(build)
        return Response(serializer.data)
    
    def update(self, request, pk):
        # build = Build.objects.get(pk=pk)
        # build.title = request.data["title"]
        # build.img = request.data["img"]
        # build.price = request.data["price"]
        # build.rating = request.data["rating"]
        
        # builder = Builder.objects.get(user=request.auth.user)
        # build.builder = builder
        # build.save()
        build = Build.objects.get(pk=pk)
        serializer = CreateBuildSerializer(build, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'title', 'img', 'price', 'rating')
        
class CreateBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'title', 'img', 'price', 'rating')