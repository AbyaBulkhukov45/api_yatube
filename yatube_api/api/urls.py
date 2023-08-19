from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = router.urls
