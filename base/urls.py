from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework_nested import routers

# router = routers.SimpleRouter()
# router.register(r'link', views.Login)
# link_router = routers.NestedSimpleRouter(router, 'link', lookup='link')


urlpatterns = [
  path('link/', views.Login.as_view({'get': 'list', 'post': 'create'})), #(?P<pk>[0-9]+)/$
 # path('link/<str:pk>/', views.Login.as_view({'get': 'list', 'post': 'create'}), name="home"),
  path('login/', views.LoginAPI.as_view()),
  path('register/', views.RegisterAPI.as_view()),
  path('delete/<str:pk>/', views.LoginAPIDestroy.as_view())
]