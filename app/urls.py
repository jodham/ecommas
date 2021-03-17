from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('store/', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
