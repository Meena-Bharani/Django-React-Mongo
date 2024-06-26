from django.shortcuts import render

# Create your views here.
from .models import Article, ArticleCategory
from .serializer import ArticleSerializer, ArticleCategorySerializer
from rest_framework.generics import ListAPIView


class ArticleCategoryList(ListAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
