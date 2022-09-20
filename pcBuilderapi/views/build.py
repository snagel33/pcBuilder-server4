from distutils.command.build import build
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pcBuilderapi.models import Build, Builder, Part, part, partType
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
        parts = request.data.get('parts', None)
        # build = Build.objects.create(
        #     title=request.data["title"],
        #     builder=builder,
        #     img=request.data["img"],
        #     price=request.data["price"],
        #     rating=request.data["rating"],
        # )
        if parts:
            del request.data["parts"]
        
        # serializer = CreateBuildSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(builder=builder)
        # build = Build.objects.get(pk=serializer.data["id"])
        # response_serializer = BuildSerializer(build)
        
        serializer = BuildSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(builder=builder)
        new_build = Build.objects.get(pk=serializer.data["id"])
        if parts:
            print(parts)
            for part_id in parts:
                print(part_id)
                # if "id" in key:
                build_part = Part.objects.get(pk=part_id)
                new_build.parts.add(build_part)
                # if "cpu" in key:
                    # new_cpu = parts.objects.get(pk=request.data[key])
                    # new_build.BuildParts.add(new_cpu)
                # elif "motherboard" in key:
                #     new_motherboard = motherboard.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_motherboard)
                # elif "memory" in key:
                #     new_memory = memory.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_memory)
                # elif "gpu" in key:
                #     new_gpu = gpu.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_gpu)
                # elif "storage" in key:
                #     new_storage = storage.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_storage)
                # elif "case" in key:
                #     new_case = case.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_case)
                # elif "psu" in key:
                #     new_psu = psu.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_psu)
                # elif "os" in key:
                #     new_os = os.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_os)
                # elif "monitor" in key:
                #     new_monitor = monitor.objects.set(pk=request.data[key])
                #     new_build.BuildParts.add(new_monitor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
    
    def destroy(self, request, pk):
        try:
            build = Build.objects.get(pk=pk)
            build.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Build.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# class PartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Part
#         fields = ('id', 'partType', 'maker', 'name', 'img', 'description', 'price')
   
class BuildSerializer(serializers.ModelSerializer):
    # parts = PartSerializer(many=True)
    class Meta:
        model = Build
        fields = ('id', 'title', 'img', 'price', 'rating', 'parts', 'builder_id')
        depth = 5
        
class CreateBuildSerializer(serializers.ModelSerializer):
    # parts = PartSerializer(many=True)
    class Meta:
        model = Build
        fields = ('id', 'title', 'img', 'price', 'rating', 'parts', 'builder_id')
        # fields = ('id', 'title', 'img', 'price', 'rating', 'builder_id', 'cpu', 'motherboard', 'memory', 'gpu', 'storage', 'case', 'psu', 'os', 'monitor')
        depth = 5