"""alphawomenProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static

from Users_app import views as users_view
from django.contrib.auth import views as  auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('register/', include('Users_app.urls')),


    path('admin-signup/', users_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name = 'Users_app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'Users_app/logout.html'), name='logout'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)