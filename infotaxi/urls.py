from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404,handler500
from django.contrib.auth import views as auth_views

from apps.webclient.views import error_404

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('auth/', include('apps.authx.urls', namespace='authx')),

    # Webclient
    path('', include('apps.webclient.urls', namespace='weblcient')),

    # API
    path('apix/', include('apps.api.urls')),

    # AUTH
    path('authx/', include('rest_framework_social_oauth2.urls')),

    # path('login/', auth_views.login, name='login'),
    # path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    # path('', include('apps.api.urls')),
    # path('api-manual/', include('apps.api.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

handler404 = error_404
handler500 = error_404