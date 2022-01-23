from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from scraper.models import Article
from scraper.serializers import ArticleSerializer
from rest_framework.decorators import api_view


@api_view(["GET", "POST", "DELETE"])
def list_articles(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == "GET":
        articles = Article.objects.all()
        articles_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)
        # 'safe=False' for objects serialization
