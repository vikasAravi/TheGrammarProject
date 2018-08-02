from django.urls import path
from application.views import index
from application.views import custom,object_specific_view
urlpatterns = [
    path('createaccount/', index , name = "signupform"),
    path('loginform/',custom, name = "loginform"),
    path('objects/<int:oid>/', object_specific_view, name = 'objects'),
    ]
