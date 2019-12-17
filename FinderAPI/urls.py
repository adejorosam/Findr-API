"""FinderAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from findr import views
from django.conf import settings
from django.conf.urls.static import static
'''
router = routers.DefaultRouter()
router.register(r'api/house', views.HouseView)
router.register(r'api/block', views.BlockView)
router.register(r'api/room', views.RoomView)
router.register(r'api/warden', views.WardenView)

'''


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^apartment/',views.ApartmentList.as_view(), name='Apartment'),
    url(r'^user/', views.UserList.as_view(), name='User'),
    #url(r'^category/',views.ApartmentCategoryList.as_view(), name='ApartmentCategory'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)