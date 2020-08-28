from django.urls import path
from apollo_app import views
urlpatterns = [
    path('login/', views.login),# 配置登录的路由规则
    path('index/', views.index),# 配置首页的路由规则
    path('safe_a/', views.safe_a),# 配置A等级安全的路由规则
]
