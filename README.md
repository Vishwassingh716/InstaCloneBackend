# InstaCloneBackend

# Authentication and Role-Based Access Control (RBAC)
This project implements a REST API with robust Authentication and Role-Based Access Control (RBAC) using the Django REST Framework (DRF). Below is an explanation of the key features, structure, and functionality.

Features

Authentication:

Utilizes JWT-based authentication provided by rest_framework_simplejwt.

Customization includes adding additional claims (e.g., email) in JWT tokens.
Role-Based Access Control (RBAC):

Permissions are enforced at the class or method level using DRF's permission_classes.

Custom permissions like IsAdminOrSelf are implemented for fine-grained control.

Endpoints with RBAC:

User management with restricted views for administrators.

CRUD operations for posts, comments, and follows with role-based access.

Specific restrictions for updating or deleting resources by the owner.

Error Handling:

Handles ObjectDoesNotExist gracefully to avoid crashes.

Returns appropriate HTTP status codes for errors.

Directory Structure

Views:

Authentication (MyTokenPairView, UserRegistrationView).

User Management (UserList, RetrieveUserView, DeleteUserView).

Post Management (PostsView, RetrievePostView, UserPostView).

Follow/Like System (FollowUserView, LikePostView).

Comments (CommentsView, RetrieveCommentView, DeleteCommentView).

Models:

The system uses models such as ProfilePage, Posts, CommentOnPost, and Followers.

-Serializers:

Serializers handle validation and transformation of request/response data for models.

-Permissions:

Built-in: IsAdminUser, IsAuthenticated, AllowAny.

Custom: Includes IsAdminOrSelf (for admin or owner-specific actions).

#Key Classes and RBAC Overview

Authentication

MyTokenPairSerializer: Adds email to the JWT payload for better context.

MyTokenPairView: Endpoint for obtaining customized JWT tokens.

-Users

UserList: Restricted to admins (IsAdminUser) to manage user data.

UserRegistrationView: Open to all (AllowAny) for new registrations.

RetrieveUserView: Authenticated users (IsAuthenticated) can view or edit their profiles.

-Posts

PostsView: Authenticated users (IsAuthenticated) can create or list posts.

RetrievePostView: Users can retrieve, update, or delete posts they own.

-Comments

CommentsView: Allows authenticated users to create comments.

RetrieveCommentView: Lists comments for a specific post.

DeleteCommentView: Authenticated users can delete their comments.

-Likes and Followers

LikePostView: Toggle likes on posts, restricted to authenticated users.

FollowUserView: Manage follow/unfollow actions, restricted to authenticated users.


-Admin or Owner Permissions
DeleteUserView: Uses a custom permission IsAdminOrSelf to allow either administrators or the user themselves to delete the account.
