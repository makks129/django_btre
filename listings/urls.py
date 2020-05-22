from django.urls import path

from . import views

urlpatterns = [
    # path here refers to /listings
    path('', views.index, name='listings'),
    # path here refers to /listings/id (e.g. /listings/123)
    path('<int:listing_id>', views.listing, name='listing'),
    # path here refers to /listings/search
    path('search', views.search, name='search')
]
