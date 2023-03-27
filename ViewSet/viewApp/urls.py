from django.contrib import admin
from django.urls import path,include
from viewApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',views.StudentViewSets,basename="student")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
]