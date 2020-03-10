
from rest_framework import serializers
from .models import  Snippet
from django.contrib.auth.models import User
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id','owner' ,'title', 'code', 'linenos', 'language', 'style']
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    class Meta:
        model = User
        #追加User表中的额外在字段,进行序列化,如何实现非当前表额外字段的添加？
        fields = ['id','username','snippets']
