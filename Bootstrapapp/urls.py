from  django.urls import path
from . import views
urlpatterns=[

path('', views.home, name='home'),
path('/meetings', views.meetings, name='meetings'),
path('/meeting_details', views.meeting_details, name='meeting_details'),

]