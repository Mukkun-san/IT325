from django.conf.urls import url
from scraper import views

urlpatterns = [
    url("api/scrape/article/", views.scrape_article),
]
