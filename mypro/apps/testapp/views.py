# Create your views here.
from .models import Snippet
from .serializers import SnippetSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .autodefine_permissions import IsOwnerOrReadOnly 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.reverse import reverse

from rest_framework import viewsets
from rest_framework.decorators import action
#@api_view(['GET'])
#def api_root(request,format=None):
#    return Response({
#       'users':reverse('user-list',request=request,format=format),
#        'snippets':reverse('snippet-list',request=request,format=format)})

class SnippetViewSet(viewsets.ModelViewSet):
    """
    this viewset automatically provides 'list','create','retrieve','update' and 'destory' actions.
    Additionally we also provide an extra 'highlight' action
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    def perform_create(self,serializer):
       serializer.save(owner=self.request.user)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This vieset automatially provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
