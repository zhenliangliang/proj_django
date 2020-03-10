# Create your views here.
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics

#@csrf_exempt
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets,or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

#@csrf_exempt
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
