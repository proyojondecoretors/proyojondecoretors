"""product_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.check),
    path('home', views.check, name='home'),
    path('auth/login', include('apps.authenticator.urls'), name='alogin'),
    path('logout', views.log_out),
    path('dashboard', views.Main_view.deshboard, name='dashboard'),
    path('manage', views.Main_view.manage, name='manage'),
    path('add', views.Main_view.add, name='add'),
    path('activeorders', views.Main_view.activeOrders, name='activeorders'),
    path('order', views.Main_view.order, name='order'),
    path('done/<slug>', views.Main_view.order_complete),

] + static('/static/', document_root=settings.MEDIA_ROOT)
