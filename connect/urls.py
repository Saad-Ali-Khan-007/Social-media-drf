from django.urls import path
from . import views 
urlpatterns = [
    path("user/",views.UserList.as_view()),
    path("user/<int:pk>",views.UserDetail.as_view()),
    path("post/",views.PostList.as_view()),
    path("user/login/",views.user_login)
]
