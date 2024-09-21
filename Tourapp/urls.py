"""
URL configuration for Touristdestination project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import DestinationDetailView,DestinationListView,register, user_login, user_logout

urlpatterns = [
    path('destinations/',views.DestinationListCreate.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', views.DestinationDetail.as_view(), name='destination-detail'),
    path('list/', views.destination_list, name='destination-list'),                  # List of destinations
    path('create/', views.destination_create, name='destination-create'),       # Create a new destination
    path('<int:pk>/update/', views.destination_update, name='destination-update'), # Update a specific destination
    path('<int:pk>/delete/', views.destination_delete, name='destination-delete'),
    path('',views.index,name='index'),
    path('index2/', views.index2, name='index2'),
    path('destination/<int:pk>/',views.DestinationDetailView.as_view, name='destination-detailview'),
    path('destinationsearch/',DestinationListView.as_view(), name='destination-search'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)