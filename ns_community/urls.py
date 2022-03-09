from django.urls import path
from ns_community import views

urlpatterns = [
    path('',views.index,name='index'),

]