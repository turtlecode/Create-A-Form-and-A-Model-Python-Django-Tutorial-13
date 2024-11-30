from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('toggle_favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),
]
