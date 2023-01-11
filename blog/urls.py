from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("login/", views.login.as_view(), name="login"),
    path("logout/", views.logout.as_view(), name="logout"),
    path("login_datos/", views.login_datos.as_view(), name="login_datos"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("mis-posts/", views.PostListUser.as_view(),name="mis-posts"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
