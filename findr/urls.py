from django.urls import path,include
from django.conf.urls import url
from findr import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as rviews
from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework_swagger.views import get_swagger_view


#schema_view = get_swagger_view(title='Findr API')


...
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    path('', views.API_Root.as_view(), name='API Root'),
    #url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('apartments/',views.ApartmentList.as_view(), name= 'ApartmentList'),
    path('apartments/<int:pk>/', views.ApartmentDetails.as_view(), name='ApartmentDetail'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='User'),
    path('login/', views.login, name='Login'),
    path('image/', views.ImageList.as_view(), name='Image' ),
    path('api-token-auth/', rviews.obtain_auth_token, name='RViews'),
    
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))
]



urlpatterns = format_suffix_patterns(urlpatterns)