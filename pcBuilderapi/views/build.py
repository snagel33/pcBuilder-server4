from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Build, Builder, builder, Part, part
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
        # cpu=request.query_params.get('cpu', None)
        # if cpu is not None:
        #         cpu = Part.objects.get(pk=cpu)
            
        # motherboard=Part.objects.get(pk=request.data["motherboard"])
        builder = Builder.objects.get(user=request.auth.user)
        parts = request.query_params.get('parts', None)
        build = Build.objects.create(
            title=request.data["title"],
            builder=builder,
            img=request.data["img"],
            price=request.data["price"],
            rating=request.data["rating"],
            parts=parts
            # cpu=cpu,
            # motherboard=motherboard
        )
        serializer = BuildSerializer(build, many=True)
        new_build = Build.objects.get(pk=serializer.data["id"])
        for key in request.data:
            if "id" in key:
                if "cpu" in key:
                    new_cpu = cpu.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_cpu)
                elif "motherboard" in key:
                    new_motherboard = motherboard.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_motherboard)
                elif "memory" in key:
                    new_memory = memory.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_memory)
                elif "gpu" in key:
                    new_gpu = gpu.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_gpu)
                elif "storage" in key:
                    new_storage = storage.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_storage)
                elif "case" in key:
                    new_case = case.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_case)
                elif "psu" in key:
                    new_psu = psu.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_psu)
                elif "os" in key:
                    new_os = os.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_os)
                elif "monitor" in key:
                    new_monitor = monitor.objects.get(pk=request.data[key])
                    new_build.BuildParts.add(new_monitor)
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
        fields = ('id', 'title', 'img', 'price', 'rating', 'parts', 'builder_id')
        depth = 5
        
class CreateBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'title', 'img', 'price', 'rating', 'parts', 'builder_id')
        depth = 5