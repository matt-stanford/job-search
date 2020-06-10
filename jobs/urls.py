from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.listings, name='listings'),
    path('search', views.search, name='search'),
    path('share_job', views.share_job, name='share_job'),
    path('shortlist', views.shortlist, name='shortlist'),
    path('delete/<int:job_id>', views.delete, name='delete'),
    path('detail/<int:job_id>', views.detail, name='detail'),
    path('remove/<int:job_id>', views.remove_from_shortlist, name='remove_from_shortlist'),
    path('add/<int:job_id>', views.add_to_shortlist, name='add_to_shortlist'),
]
