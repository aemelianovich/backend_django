from django.urls import path
from . import views

urlpatterns = [
    # By default /listings it will be added into main real estate project in the settings
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
