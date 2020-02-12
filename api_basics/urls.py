from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    
    path('function/articles/', views.article_list, name='article_list'), 
    path('class/articles/', views.ArticleAPIView.as_view(), name='article'),
    path('function/details/<int:pk>/', views.article_details, name='article_details'),  
    path('class/details/<int:id>/', views.ArticleDetails.as_view(), name='article_details'),
    path('generic/articles/<int:id>/', views.GenericAPIView.as_view(), name='generic') 
]