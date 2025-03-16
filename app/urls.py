from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from polls.models import Post, Comment

# Сериализатор для модели Post
class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Показываем имя автора

    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'author', 'created_at', 'updated_at']


# Сериализатор для модели Comment
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Показываем имя автора

    class Meta:
        model = Comment
        fields = ['url', 'text', 'author', 'created_at', 'post']


# ViewSet для модели Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# ViewSet для модели Comment
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Роутер для автоматической генерации URL
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)  # Регистрируем ViewSet для Post
router.register(r'comments', CommentViewSet)  # Регистрируем ViewSet для Comment

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),  # Маршруты API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Авторизация
]