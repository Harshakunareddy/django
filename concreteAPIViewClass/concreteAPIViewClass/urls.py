"""concreteAPIViewClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from concreteAPIViewClassApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',include('concreteAPIViewClassApp.urls')),
    path("list/",studentList.as_view()),
    path("create/",studentCreate.as_view()),
    path("retrieve/<int:pk>/",studentRetrieve.as_view()),
    path("destroy/<int:pk>/",studentDestroy.as_view()),
    path("update/<int:pk>/",studentUpdate.as_view()),
    #............
    path("listcreate/",studentListCreate.as_view()),
    path("redes/<int:pk>/",studentRetrieveDestroy.as_view()),
    path("reup/<int:pk>/",studentRetrieveUpdate.as_view()),
    path("reupde/<int:pk>/",studentRetrieveUpdateDestroy.as_view()),

]
