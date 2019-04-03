# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
app_name = 'ck_app'


router.register('subject', views.SubjectView) #(endpoint, url request)
router.register('article', views.ArticleView)

urlpatterns = [
    path('', include(router.urls)), #urls are automatically generatated 
    path('v1/subjects/', include('rest_framework.urls', namespace='subject')),
    path('v1/articles/', include('rest_framework.urls', namespace='article')),
]
