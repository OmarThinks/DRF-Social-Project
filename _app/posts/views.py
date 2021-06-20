from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer
from _app.default_values import MyPagination

# Create your views here.
# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class  = MyPagination