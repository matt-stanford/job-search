from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('uploadcv/', views.resume_upload, name='uploadcv'),
    path('downloadcv/<filepath>', views.resume_download, name='downloadcv'),
    path('signin/', views.loginView, name='login'),
    path('signout/', views.logoutView, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
