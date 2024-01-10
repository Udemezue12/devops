from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    # path('', TemplateView.as_view(template_name='core/index.html')),
    path('', views.homepage, name =''),
    path('register',views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name="user-logout"),





]
