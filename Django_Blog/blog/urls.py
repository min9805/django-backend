from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Post', views.IntruderImage)
routers.register('NameCount', views.IncrementNameCountView)


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('confirm', views.confirm_post_list, name='confirm_post_list'),
    path('api/confirm', views.api_confirm_post_list, name='confirm_post_list'),
    path('api_root/', include(routers.urls)),
    path('analytics', views.main_page, name='main_page'),   
    path('post/<int:pk>/save/', views.post_save, name='post_save'),
    path('post/<int:pk>/discard/', views.post_discard, name='post_discard'),
]
