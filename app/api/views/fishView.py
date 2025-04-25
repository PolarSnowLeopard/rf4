from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from fish.models import Fish
from api.serializers.fishSerializer import FishSerializer

@api_view(['GET', 'POST'])
def fish_list(request):
    if request.method == 'GET':
        fish = Fish.objects.all()
        serializer = FishSerializer(fish, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fish_detail(request, name: str):
    try:
        fish = Fish.objects.get(name=name)
    except Fish.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FishSerializer(fish)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FishSerializer(fish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
