from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.listings, name='listings'),
    path('search', views.search, name='search'),
    path('shortlist', views.shortlist, name='shortlist'),
]
