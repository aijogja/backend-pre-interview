from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response as response
from .models import Record
from .serializers import RecordSerializer, DataSerializer
from .parsers import ListXMLParser
# Create your views here.

@api_view(['POST'])
def echo(request):
    """
    Request json data and return it
    """
    if request.method == 'POST':
        data = request.data
        if data:
            return response(data, status=200, content_type=request.content_type)
        return response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([ListXMLParser])
def receive(request):
    """
    Request xml data and response json
    """
    data = request.data
    serializer = RecordSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        record = serializer.save()
        data_serializer = DataSerializer(record.data_set.all(), many=True)
        return response(data_serializer.data, status=200)


@api_view(['GET'])
def display(request, id):
    """
    Response json data
    """
    try:
        record = Record.objects.get(pk=id)
        serializer = DataSerializer(record.data_set.all(), many=True)
        return response(serializer.data, status=200)
    except Record.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)
