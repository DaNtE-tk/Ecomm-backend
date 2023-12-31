from django.urls import path
import base.views.user_views as views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     # TokenRefreshView,
# )

# app_name = "base"

urlpatterns = [
    # path('',views.getRoutes,name="routes"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    

    path('register/',views.registerUser,name="register"),
   
   
    path('',views.getUsers,name="users"),
   
    path('profile/',views.getUserProfile,name="user-profile"),
    path('profile/update/',views.updateUserProfile,name="user-profile-update"),
    
    path('<str:pk>/', views.getUserById, name="user"),
    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name="user-delete"),
    # path('products/',views.getProducts,name="products"),
    # path('products/<str:pk>',views.getProduct,name="product")
]