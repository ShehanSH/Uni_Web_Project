from django.urls import path
from . import views

urlpatterns = [
    path('create_sports_item_request/', views.create_sports_item_request, name='create_sports_item_request'),

]
