# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Subject, Article

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', 'color')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('hero_image', 'id', 'title', 'subject', 'publish_date', 'author', 'content')
        
