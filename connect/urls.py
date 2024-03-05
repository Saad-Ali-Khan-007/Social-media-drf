from django.urls import path
from . import views 
urlpatterns = [
    path("user/",views.UserList.as_view()),
    path("user/<int:pk>",views.UserDetail.as_view()),
    path("post/",views.PostList.as_view()),
    path("user-post/",views.UserPostList.as_view()),
    path("post/<int:pk>",views.PostDetail.as_view()),
    path("user-post/<int:pk>",views.UserPostDetail.as_view()),
    path("user/login/",views.user_login)
]
