from rest_framework import serializers
from .models import Note

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['headline', 'topic', 'details', 'datetime_created', 'datetime_updated', 'user']
        model = Note
        