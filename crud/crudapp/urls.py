from django.urls import path
from .views import *
urlpatterns = [
    path('',Booklist),
    path('add/',Booklist_post),
    path('up/<int:id>/',Booklist_update),
    path('del/<int:id>/',Booklist_delete),
]
