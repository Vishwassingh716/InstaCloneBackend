from django.urls import path
from .views import *

from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('userslistt/',UserList.as_view(),name = "userlistt"),
    path('token/', MyTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('user/retrieve/<int:pk>/',RetrieveUserView.as_view(), name = 'retrieve'),
    path('posts/',PostsView.as_view(), name = 'post'),
    path('posts/retrieve/<int:pk>',RetrievePostView.as_view(), name = 'post'),
    path('userposts/<int:pk>',UserPostView.as_view(), name = 'userpost'),
    path('likepost/<int:pk>',LikePostView.as_view(), name = 'userpost'),
    path('post/likes/<int:pk>',RetrieveUserswholikedView.as_view(), name = 'userpost'),
    path('user/follow/<int:pk>',FollowUserView.as_view(), name = 'followuser'),
    path('user/followers/<int:pk>',RetrieveUserWhoFollowView.as_view(), name = 'followers'),
    path('post/comment/<int:pk>',CommentsView.as_view(), name = 'comment'),
    path('comments/post/<int:pk>',RetrieveCommentView.as_view(), name = 'commentsonpost'),
    path('delete/comment/<int:pk>',DeleteCommentView.as_view(), name = 'deletecomment'),
    path('delete/user/<int:pk>',DeleteUserView.as_view(), name = 'deleteuser'),

]



    