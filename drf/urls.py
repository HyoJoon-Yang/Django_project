from django.urls import path
from .views import PostViewSet

# Post 목록 보여주기
blog_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Post detail 보여주기 + 수정 + 삭제
blog_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('post/', blog_list),
    path('post/<int:pk>/', blog_detail),
]

# from rest_framework import routers
# from drf import views
# from django.urls import include, re_path

# router = routers.DefaultRouter()
# router.register(r'test/posts', views.PostViewSet)  # crud관련된 메소드를 다 쓸거에요   


# urlpatterns = [
#     re_path(r'^drf/',include(router.urls)), # drf/로 시작하는 모든 경로는 router.url 을 참조해주세요  
# ]