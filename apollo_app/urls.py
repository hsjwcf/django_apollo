from django.urls import path
from apollo_app import views
urlpatterns = [
    path('login/', views.login),# 配置登录的路由规则
    path('index/', views.index),# 配置首页的路由规则
    path('safe_a/', views.safe_a),# 配置A等级安全的路由规则
    path('safe_b/', views.safe_b),# 配置B安全等级的路由规则
    path('reg/', views.reg),# 配置注册功能的路由规则
]
