from django.urls import path
from .views import CDRListAPIView

urlpatterns = [
    path('api/cdrs/', CDRListAPIView.as_view(), name='cdr-list'),
]