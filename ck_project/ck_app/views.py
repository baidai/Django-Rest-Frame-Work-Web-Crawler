#from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Subject, Article
from .serializers import SubjectSerializer, ArticleSerializer


class SubjectView(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all() #query command in database
    serializer_class = SubjectSerializer
    pagination_class = None 
    
class ArticleView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all() #query command in database
    serializer_class = ArticleSerializer
    ordering_fields = ('publish_date')