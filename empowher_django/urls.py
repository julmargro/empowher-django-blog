"""
URL configuration for empowher_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('register/', blog_views.register, name='register'),
    path('login/', blog_views.login_view, name='login'),
    path('logout/', blog_views.logout_view, name='logout'),
    path('post/<int:pk>/', blog_views.post_detail, name='post-detail'),
    path('post/new/', blog_views.create_post, name='create-post'),
    path('post/<int:pk>/update/', blog_views.update_post, name='update-post'),
    path('post/<int:pk>/delete/', blog_views.delete_post, name='delete-post')
]
