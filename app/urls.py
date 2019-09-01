from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('table/', views.table, name='table_page'),
    path('stat/', views.start, name='stats_page'),
    path('api/', views.load_graph_data, name='api_load_graph_data'),
]
