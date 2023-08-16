from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date',
            'author', 'image', 'group'
        )
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('slug',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        required=False
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'text', 'post',
            'author', 'created'
        )
