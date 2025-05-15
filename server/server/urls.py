from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('workspace/', include('workspace.urls')),
    path('tag/', include('tag.urls')),
]
