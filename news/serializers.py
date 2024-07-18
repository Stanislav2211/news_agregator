from rest_framework import serializers
from .models import BBC,HackerNews
from rest_framework.fields import CharField, URLField

class BbcSerializer(serializers.ModelSerializer):
    title = CharField()
    article = CharField()
    url = URLField(read_only=True)
    class Meta:
        model = BBC
        fields = ('title', 'article', 'url')

class HackerNewsSerializer(serializers.ModelSerializer):
    title = CharField()
    points = CharField()
    author = CharField()
    url = URLField(read_only=True)
    class Meta:
        model = HackerNews
        fields = ('title', 'points', 'author', 'url')