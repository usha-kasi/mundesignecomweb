from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import order_history

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('my_account/', views.my_account, name='my_account'),
    path('order_history/', views.order_history, name='order_history'),
    path('saved_addresses/', views.saved_addresses, name='saved_addresses'),
    path('saved_payment_details/', views.saved_payment_details, name='saved_payment_details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('order/<int:order_id>/', views.individual_order, name='individual_order'),
    path('return_order/', views.return_order, name='return_order'),
    path('order-history-json/', views.order_history_json, name='order_history_json'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

