from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('logout/', auth_views.LogoutView.as_view(),name='logout'),
        path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
        path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change password'),
        path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='password_change_done' )
       
]