from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Post', views.blogImage, basename='Post')
# router.register('View', views.UserViewSet, basename='view')
router.register('search', views.imagePostSearch, basename='search')


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('api_root/', include(router.urls)),
]
