from rest_framework import routers
from rest_framework.documentation import include_docs_urls
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from api.views import ArticleViewSet, UserViewSet

router = routers.DefaultRouter()

# register routers
router.register('article', ArticleViewSet)
router.register('users', UserViewSet)