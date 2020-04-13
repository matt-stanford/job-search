from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.listings, name='listings'),
    path('search', views.search, name='search'),
    path('shortlist', views.shortlist, name='shortlist'),
    path('delete/<int:job_id>', views.delete, name='delete'),
    path('add/<int:job_id>', views.add_to_shortlist, name='add_to_shortlist'),
]
