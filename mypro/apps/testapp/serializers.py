
from rest_framework import serializers
from .models import  Snippet
from django.contrib.auth.models import User
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')
    class Meta:
        model = Snippet
        fields = ['url','id','highlight','owner' ,'title', 'code', 'linenos', 'language', 'style']
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)
    class Meta:
        model = User
        #追加User表中的额外在字段,进行序列化,如何实现非当前表额外字段的添加？
        fields = ['url','id','username','snippets']
