from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RegisterView,  LoginView, LogoutView, UserDetailView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .views import ProductListView, ProductDetailView, ProductCreateView, CategoryListView, CategoryDetailView, CategoryCreateView, UserDetailView
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView, OrderItemListView, OrderItemDetailView, OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView
from .views import ProductImageUploadView, ProductImageDetailView, ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from .views import ShippingAddressListView, ShippingAddressDetailView, ShippingAddressCreateView, ShippingAddressUpdateView, ShippingAddressDeleteView
from .views import PromotionListView, PromotionDetailView, PromotionCreateView, PromotionUpdateView, PromotionDeleteView
router = DefaultRouter()


urlpatterns = [

    # API pour les produits
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),


    # API pour les catégories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),

    # API pour l'authentification
    path('auth/registration/', RegisterView.as_view(), name='auth-registration'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/user/', UserDetailView.as_view(), name='auth-user-detail'),
    path('auth/password/change/', PasswordChangeView.as_view(), name='auth-password-change'),
    path('auth/password/reset/', PasswordResetView.as_view(), name='auth-password-reset'),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='auth-password-reset-confirm'),

    # API pour les commandes
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),

    # API pour les articles de commande
    path('order-items/', OrderItemListView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),
    path('order-items/', OrderItemCreateView.as_view(), name='order-item-create'),
    path('order-items/<int:pk>/', OrderItemUpdateView.as_view(), name='order-item-update'),
    path('order-items/<int:pk>/', OrderItemDeleteView.as_view(), name='order-item-delete'),


    # API pour les images des produits
    path('products/upload-image/', ProductImageUploadView.as_view(), name='product-image-upload'),
    path('products/images/<int:pk>/', ProductImageDetailView.as_view(), name='product-image-detail'),

    # API pour les commentaires et évaluations des produits
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),


    # API pour les adresses de livraison
    path('shipping-addresses/', ShippingAddressListView.as_view(), name='shipping-address-list'),
    path('shipping-addresses/<int:pk>/', ShippingAddressDetailView.as_view(), name='shipping-address-detail'),
    path('shipping-addresses/', ShippingAddressCreateView.as_view(), name='shipping-address-create'),
    path('shipping-addresses/<int:pk>/', ShippingAddressUpdateView.as_view(), name='shipping-address-update'),
    path('shipping-addresses/<int:pk>/', ShippingAddressDeleteView.as_view(), name='shipping-address-delete'),

    # API pour les promotions
    path('promotions/', PromotionListView.as_view(), name='promotion-list'),
    path('promotions/<int:pk>/', PromotionDetailView.as_view(), name='promotion-detail'),
    path('promotions/', PromotionCreateView.as_view(), name='promotion-create'),
    path('promotions/<int:pk>/', PromotionUpdateView.as_view(), name='promotion-update'),
    path('promotions/<int:pk>/', PromotionDeleteView.as_view(), name='promotion-delete'),

]
