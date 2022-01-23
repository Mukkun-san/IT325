from cgitb import html
from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from scraper.models import Article
from scraper.serializers import ArticleSerializer
from rest_framework.decorators import api_view


from bs4 import BeautifulSoup
import requests


@api_view(["POST"])
def scrape_article(request):
    # Scrape an article from given URL and save to DB if not already exists
    if request.method == "POST":
        url = JSONParser().parse(request)["url"]
        print(url)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        title = soup.find(
            "h1",
            attrs={"class": "m-detail-header--title"},
        ).get_text()

        if Article.objects.filter(title=title).exists():
            return JsonResponse(
                {"DUPLICATE ERROR": "ARTICLE ALREADY EXISTS"},
                status=status.HTTP_409_CONFLICT,
            )
        articleEl = soup.find(
            "div",
            attrs={"class": "m-detail--body"},
        )
        content = ""
        for el in articleEl.children:
            if el.name == "p":
                content += el.get_text()
        article_serializer = ArticleSerializer(
            data={"title": title, "content": content}
        )
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(
            article_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
        # 'safe=False' for objects serialization
