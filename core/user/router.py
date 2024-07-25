from rest_framework.routers import DefaultRouter

from core.user.views import UserViewSet

app_name = "user"

router = DefaultRouter()
router.register("user", UserViewSet)