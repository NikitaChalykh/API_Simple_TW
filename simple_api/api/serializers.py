from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    is_favorited = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'date', 'is_favorited')

    def get_is_favorited(self, obj):
        if obj.favorite_posts.filter(
                user=self.context['request'].user
        ).exists():
            return True
        return False
