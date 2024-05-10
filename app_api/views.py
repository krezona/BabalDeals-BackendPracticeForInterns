from rest_framework import generics
from app.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAuthenticated, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions

class PostUserWritePermission(BasePermission):
    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
        


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer


#     def get_object(self,queryset = None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, title=item)
    
    
#     #define custom queryset
#     def get_queryset(self):
#         return Post.objects.all()




# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)


#     def retrive(self,request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)





class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author = user)
    


class PostDetail(generics.ListAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    

    serializer_class = PostSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)

        
        return Post.objects.filter(title=title)

class PostListDetailfilter(generics.ListAPIView):
    

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']




class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

