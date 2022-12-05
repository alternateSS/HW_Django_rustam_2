from django.urls import path

from . import views

urlpatterns = [
    path('shop/greetings/', views.greetings, name='greetings'),
    path('shop/', views.list_item, name='list_item'),
    path('shop/<int:id>/', views.detail_item, name='detail_item'),

]