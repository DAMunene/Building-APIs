from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.drink_list, name = 'beverages' ),
    path('<int:id>/', views.drink_detail, name = 'beverage_detail' ),


]

urlpatterns = format_suffix_patterns(urlpatterns)