

from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', views.FBV),
    path('do/<int:pk>', views.FBV_pk),
    path('do-class/', views.CBV_list.as_view()),
    path('do-class/<int:pk>', views.CBV_pk.as_view()),
    path('search/', views.search),
    path('reservation/', views.new_reservation),
    

]
