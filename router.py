from rest_framework.routers import DefaultRouter

from core.user.views import UserViewSet

app_name = "core.user"

router = DefaultRouter()
router.register("usuarios", UserViewSet)