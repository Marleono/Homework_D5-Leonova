from django.urls import path
from .views import Posts, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, IndexView
from .views import upgrade_me

urlpatterns = [
    path('', Posts.as_view()),
    path('search/', Posts.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='news_detail'), # Ссылка на детали товара
    path('add/', PostCreateView.as_view(), name='news_add'), # Ссылка на создание товара
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='news_add'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='news_delete'),
    path('upgrade/', upgrade_me, name = 'upgrade'),


]