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
    path('<str:pk>/',views.getProduct,name="product")
]