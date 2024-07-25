from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.user.router import router 
from core.sendEmail.views import EmailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/email/', EmailAPIView.as_view(), name='email'),
]
