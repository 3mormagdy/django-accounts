from django.urls import path
from . import views
from .models import Profile

app_name = 'accounts'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]
