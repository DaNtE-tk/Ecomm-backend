from django.urls import path
import base.views.product_views as views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     # TokenRefreshView,
# )

# app_name = "base"

urlpatterns = [
    # path('',views.getRoutes,name="routes"),
    # path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    

    # path('users/register/',views.registerUser,name="register"),
   
   
    # path('users/',views.getUsers,name="users"),
    # path('users/profile/',views.getUserProfile,name="user-profile"),
    
    
    path('',views.getProducts,name="products"),
    path('create/',views.createProduct,name="product-create"),
    path('upload-image/',views.uploadImage,name="product-upload-image"),
    
    path('<str:pk>/reviews/',views.createProductReview,name="product-review"),
    path('<str:pk>/',views.getProduct,name="product"),

    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),
    path('update/<str:pk>/', views.updateProduct, name='product-update'),
    
]