from django.urls import path
from matrivume_profile import views

app_name = 'matrivume_profile'

urlpatterns = [
    path('', views.profile_view, name="profile_view"),
    path('update/', views.profile_update_view, name="profile_update_view"),
    path('registrations/', views.user_registration_view, name="registration"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]
