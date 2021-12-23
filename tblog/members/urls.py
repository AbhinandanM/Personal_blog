from django.urls import path
from members.views import UserRegistrationView, UserUpdateView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('registration/', UserRegistrationView.as_view(), name='register',),
    path('edit_profile/', UserUpdateView.as_view(), name='edit-profile',),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path( 'reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path( 'reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path( 'reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path( 'reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]