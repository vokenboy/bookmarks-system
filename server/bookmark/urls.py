from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.get_bookmarks),
    path('get/<int:pk>', views.get_bookmark),
    path('add/', views.post_bookmark),
    path('update/<int:pk>/', views.update_bookmark),
    path('delete/<int:pk>', views.delete_bookmark),
]