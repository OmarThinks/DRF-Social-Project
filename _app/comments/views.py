from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer


# Create your views here.
# ViewSets define the view behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
