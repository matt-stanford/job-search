from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('uploadcv/', views.resume_upload, name='uploadcv'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
