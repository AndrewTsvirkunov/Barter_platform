from django.urls import path, include
from .views import create_ad, edit_ad, delete_ad, ad_list, AdViewSet, ExchangeProposalViewSet
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()
router.register(r'ads', AdViewSet)
router.register(f'proposals', ExchangeProposalViewSet)

urlpatterns = [
    path('', ad_list, name='ad_list'),
    path('create/', create_ad, name='create_ad'),
    path('edit/<int:ad_id>/', edit_ad, name='edit_ad'),
    path('delete/<int:ad_id>/', delete_ad, name='delete_ad'),
    path('api/', include(router.urls), name='api'),  # API URL
]