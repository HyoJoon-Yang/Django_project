from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer  # 부가기능이니기 때문에 views와 별개파일로 관리하는 편입니다.
from .models import Post

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema_view
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers, status

@extend_schema_view(
    list=extend_schema(summary="이런식으로 class레벨 데코레이터로 문서 커스터마이징 가능하다.", tags=["사용자"]),
    i_am_custom_api=extend_schema(
        summary="@action API도 마찬가지로 class 데코레이터로 문서 커스터마이징 가능하다.",
        tags=["사용자"],
        request=PostSerializer,
        responses={status.HTTP_200_OK: PostSerializer},
    ),
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer