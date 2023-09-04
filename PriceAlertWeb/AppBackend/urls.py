from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'userDetails', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('userDetails/', views.UserViewSet, name='rest_framework'),
    path('userCreate/', views.UserCreate, name='rest_framework'),
]