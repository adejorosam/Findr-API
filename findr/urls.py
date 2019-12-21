from django.urls import path,include
from django.conf.urls import url
from findr import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as rviews
from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework_simplejwt.views import TokenObtainPairView
#from rest_framework_simplejwt.views import TokenRefreshView
#from rest_framework_simplejwt.views import verify_jwt_token

'''
    url('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/<str:phone>/register', views.VerifyPhone.as_view()),
    #path('api/<str:phone>/verify', views.VerifyPhone.as_view() ),
    '''
urlpatterns = [
    path('', views.API_Root.as_view()),
    path('apartments/',views.ApartmentList.as_view(), name= 'ApartmentList'),
    path('apartments/<int:pk>/', views.ApartmentDetails.as_view(), name='ApartmentDetail'),
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='User'),
    path('login', views.LoginView.as_view(), name='login'),
    path('api-token-auth/', rviews.obtain_auth_token, name='RViews'),
    #url(r'^category/',views.ApartmentCategoryList.as_view(), name='ApartmentCategory'),
    
    
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls'))
]



urlpatterns = format_suffix_patterns(urlpatterns)