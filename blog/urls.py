from django.urls import path
from .views import home , blog , about , contact , blog_detail

urlpatterns = [
    path('', home, name="home"),
    path('blog/', blog , name="blog"),
    path('blog/<slug:slug>/', blog_detail , name="blog_detail"),
    path('about/', about, name="about"),
    path('contact/', contact , name="contact"),
]
