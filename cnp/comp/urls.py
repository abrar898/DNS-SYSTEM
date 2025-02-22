# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('react-form/', views.react_form, name='react-form'),
    path('react-table/', views.react_table, name='react-table'),
    path('search/', views.search_results, name='search-results'),
    path('search-form/', views.search, name='search-form'),
    path('react-delete/<int:react_id>/', views.react_delete, name='react-delete'),
]
