from rest_framework import serializers
from .models import Post

# - 쿼리셋, 모델 인스턴스 등의 복잡한 데이터를 json, xml 등의 데이터로 변환해준다.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'created_at', 'updated_at', 'author', 'category', 'tag')
