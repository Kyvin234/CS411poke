"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from users import views as user_views
from users.views import team_lview, team_cview, team_delview, team_uview, forum_lview
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('team/', team_lview.as_view(), name = 'team'),
    path('team/create/', team_cview.as_view(), name = 'team-create'),
    path('team/delete/<int:pk>', team_delview.as_view(), name = 'team-delete'),
    path('team/update/<int:pk>', team_uview.as_view(), name = 'team-update'),
    path('forum/', forum_lview.as_view(), name = 'forum'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('ajax/get_pokeinfo', user_views.get_pokeinfo, name='get_pokeinfo'),
    path('', include('pokewiki.urls'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
