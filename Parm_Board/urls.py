from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('search_linkage_pc_name/', views.search_linkage_pc_name, name='search_linkage_pc_name'),
    path('search_linkage_camera_ip/', views.search_linkage_camera_ip, name='search_linkage_camera_ip'),
    path('search_linkage_model_name/', views.search_linkage_model_name, name='search_linkage_model_name'),
    path('search_linkage_func_ip_or_mura_ip/', views.search_linkage_func_ip_or_mura_ip, name='search_linkage_func_ip_or_mura_ip'),
    path('search_linkage_pattern_name/', views.search_linkage_pattern_name, name='search_linkage_pattern_name'),
    ]
