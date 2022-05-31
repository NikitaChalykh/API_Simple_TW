from django.urls import include, path

from .views import FollowViewSet, PostViewSet

app_name = 'api'


urlpatterns = [
    path('posts/', PostViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='post'),
    path('posts/<int:post_id>/favorite/', FollowViewSet.as_view({
        'post': 'create',
        'delete': 'destroy'
    }), name='favorite'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
