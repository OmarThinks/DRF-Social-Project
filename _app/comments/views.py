from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer

from _app.default_values import MyPagination

# Create your views here.
# ViewSets define the view behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class  = MyPagination
