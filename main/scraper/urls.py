from django.conf.urls import url
from scraper import views

urlpatterns = [
    url(r"^api/articles$", views.list_articles),
]
