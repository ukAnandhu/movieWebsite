from django.urls import path

from .views import register,custom_login,custom_logout,edit_profile, view_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='logout'),

    path('view_profile/',view_profile,name='view_profile'),
    path('view_profile/edit/',edit_profile,name='edit_profile'),
]