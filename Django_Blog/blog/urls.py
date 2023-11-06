from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('Post', views.IntruderImage)
routers.register('NameCount', views.IncrementNameCountView)


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api_root/', include(routers.urls)),
    path('analytics', views.main_page, name='main_page'),   
]
