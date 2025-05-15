from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.get_tags),
    path('add', views.post_tag),
    path('delete/<int:pk>', views.delete_tag),
]