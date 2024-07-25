
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
