from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostDataSerializer
from .models import PostData
from .parsers import PlainTextParser


class PostDataList(APIView):
    # Input was referenced to as a 'value', assuming plaintext
    parser_classes = [PlainTextParser]

    def get(self, request):
        model = PostData.objects.all()
        serializer = PostDataSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.data:
            return Response('No data provided', status=status.HTTP_400_BAD_REQUEST)

        # No value encoding was specified, assuming UTF-8
        serializer = PostDataSerializer(data={'post_data': request.data.decode('utf8')})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
