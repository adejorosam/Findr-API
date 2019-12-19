from django.urls import path,include
from django.conf.urls import url
from findr import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as rviews
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root),
    path('apartments/',views.ApartmentList.as_view()),
    path('apartments/<int:pk>/', views.ApartmentDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('api-token-auth/', rviews.obtain_auth_token),
    #url(r'^category/',views.ApartmentCategoryList.as_view(), name='ApartmentCategory'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

