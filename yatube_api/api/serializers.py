from rest_framework import serializers

import datetime as dt

from posts.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'
