from django.urls import path
from matrivume_profile import views

app_name = 'matrivume_profile'

urlpatterns = [
    path('registrations/', views.user_registration_view, name="registration"),
    path('login/', views.login_view, name="login")
]
