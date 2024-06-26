from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer
from .models import *


class ArticleSerializer(ModelSerializer):
    # def validate(self, data):
    #     return data

    # def create(self, validate_data):
    #     createdby = validate_data.get('createdBy', None)
    #     article = Article.objects.create(**validate_data)
    #     return article

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategorySerializer(ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'
