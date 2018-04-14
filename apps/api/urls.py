from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from apps.api.views import TaxiViewSet
from apps.api import views
from rest_framework import routers

from apps.api.views import TaxiViewSet, UserViewSet

# router = routers.DefaultRouter()
# router.register('taxis', TaxiViewSet)
# router.register('users', UserViewSet)

urlpatterns = (
    # path('', include(router.urls)),
    path('taxi/lista/', views.TaxiAppList.as_view()),
    path('taxi/buscar/', views.search_taxi),

)

# urlpatterns = format_suffix_patterns([
#     # basadas en funcion
#     # path('', views.api_root),
#     # path('fbv/taxis/', views.taxi_list),
#     # path('fbv/taxis/<int:pk>', views.taxi_detail),
#
#     # basadas en en clase APIView
#     # path('cbv/taxis/', views.TaxiList.as_view()),
#     # path('cbv/taxis/<int:pk>', views.TaxiDetail.as_view()),
#
#     # basadas en en clase GenericApiView mas Mixins
#     # path('cbv/mixin/taxis/', views.TaxiListMixin.as_view()),
#     # path('cbv/mixin/taxis/<int:pk>', views.TaxiDetailMixin.as_view()),
#
#     # basadas en en clase genericas
#     #path('cbv/generic/taxis/', views.TaxiListGeneric.as_view(), name="taxi-list"),
#     #path('cbv/generic/taxis/<int:pk>', views.TaxiDetailGeneric.as_view(), name='taxi-detail'),
#
#     # vistas de usuario
#     #path('users/', views.UserList.as_view(), name='user-list'),
#     #path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
# ])
