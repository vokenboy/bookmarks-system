from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.get_workspaces),
    path('get/<int:pk>', views.get_workspace),
    path('add/', views.post_workspace),
    path('update/<int:pk>', views.update_workspace),
    path('delete/<int:pk>', views.delete_workspace),
]