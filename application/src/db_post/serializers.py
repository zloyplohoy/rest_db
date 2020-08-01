from rest_framework import serializers
from db_post.models import PostData


class PostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostData
        fields = '__all__'
