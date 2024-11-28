#Overview

File Location: urls.py

Purpose: Maps HTTP request paths to corresponding Django views.

Authentication: Includes JWT-based endpoints for login and token refresh.

RBAC: Integrated into views via permissions, ensuring that access is controlled per role and user context.

#URL Patterns

Authentication Endpoints


Token Obtain:

Path: /token/

View: MyTokenPairView

Description: Generates a JWT token upon valid user credentials.


Token Refresh:

Path: /token/refresh/

View: TokenRefreshView

Description: Refreshes an expired JWT token.


User Management

User List:

Path: /userslistt/

View: UserList

Description: Lists all users (admin-only access).


Register User:

Path: /register/

View: UserRegistrationView

Description: Allows new user registration.

Retrieve User:
Path: /user/retrieve/<int:pk>/
View: RetrieveUserView
Description: Fetch or update user details by ID (authenticated users).
Delete User:
Path: /delete/user/<int:pk>/
View: DeleteUserView
Description: Delete a user (admin or self-permission required).
Post Management
Posts List/Create:
Path: /posts/
View: PostsView
Description: Lists or creates posts (authenticated users).
Retrieve Post:
Path: /posts/retrieve/<int:pk>/
View: RetrievePostView
Description: Fetch, update, or delete a post by ID.
User's Posts:
Path: /userposts/<int:pk>/
View: UserPostView
Description: Lists posts by a specific user.
Like Functionality
Like Post:
Path: /likepost/<int:pk>/
View: LikePostView
Description: Toggles like on a post (authenticated users).
Retrieve Users Who Liked:
Path: /post/likes/<int:pk>/
View: RetrieveUserswholikedView
Description: Lists users who liked a post.
Follow System
Follow/Unfollow User:
Path: /user/follow/<int:pk>/
View: FollowUserView
Description: Follows or unfollows a user (authenticated users).
Retrieve Followers:
Path: /user/followers/<int:pk>/
View: RetrieveUserWhoFollowView
Description: Lists followers of a user.
Comments Management
Add Comment:
Path: /post/comment/<int:pk>/
View: CommentsView
Description: Adds a comment to a post (authenticated users).
Retrieve Comments:
Path: /comments/post/<int:pk>/
View: RetrieveCommentView
Description: Lists comments for a post.
Delete Comment:
Path: /delete/comment/<int:pk>/
View: DeleteCommentView
Description: Deletes a comment (authenticated users).
