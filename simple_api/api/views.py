from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from posts.models import FavoritePost, Post

from .serializers import PostSerializer


class PostViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class FollowViewSet(viewsets.ViewSet):

    def create(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.author != request.user and (
            not request.user.favorite_posts.filter(post=post).exists()
        ):
            FavoritePost.objects.create(
                post=post,
                user=request.user
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        data_follow = request.user.favorite_posts.filter(post=post)
        if data_follow.exists():
            data_follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
