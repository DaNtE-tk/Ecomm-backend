from django.urls import path
import base.views.order_views as views


urlpatterns = [
    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='order-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='order-pay'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-deliver')
]