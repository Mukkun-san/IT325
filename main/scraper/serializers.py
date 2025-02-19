from rest_framework import serializers
from scraper.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
            "date",
        )
