from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"