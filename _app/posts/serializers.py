from rest_framework import serializers
from .models import Post


from comments.serializers import CommentSerializer

# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    #comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        #fields = "__all__"
        fields = ('id',"author" ,'content', "comments")