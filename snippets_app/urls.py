from django.urls import path
from . import views

urlpatterns = [
    path('snippets_list/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('comments/', views.comment_list),
]