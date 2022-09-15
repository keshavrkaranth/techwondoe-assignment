from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('company', views.CompanyViewSet, 'company')
router.register('team', views.TeamViewSet, 'team')

urlpatterns = router.urls + [
    path('', views.homePage),
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.register)
]
