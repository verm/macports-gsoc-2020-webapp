from django.urls import path, include
from django.views.generic.base import RedirectView

from ports.user import views

urlpatterns = [
    path('profile/', views.profile, name='account_profile'),
    path('my_ports/github/', views.my_ports_github, name='my_ports_github'),
    path('my_ports/', RedirectView.as_view(pattern_name='my_ports_github'), name='my_ports'),
    path('my_ports/email/', views.my_ports_email, name='my_ports_email'),
    path('followed_ports/', views.followed_ports, name='followed_ports'),
    path('notifications/', views.notifications_all, name='notifications'),
    path('notifications/unread/', views.notifications_all, name='notifications_unread')
]
