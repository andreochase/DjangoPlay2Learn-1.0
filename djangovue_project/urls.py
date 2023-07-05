from django.contrib import admin
from django.urls import path, include
from allauth.account import urls
from contact import views as contact_views


urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # User Management
    path('accounts/', include('allauth.urls'), name='accounts'),
    path('users/', include('users.urls')),
    # Games
    path('', include("games.urls")),
    # Contact
    path('contact/', contact_views.contact_view, name='contact'),
    # Review
    #path('reviews/', include('reviews.urls')),
    path('review/', include('review.urls')),
]
