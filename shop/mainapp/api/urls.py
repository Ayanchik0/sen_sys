from django.urls import path

from .api_views import *


urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
    path('anti_theft_systems/', Anti_theft_systemsListAPIView.as_view(), name='anti_theft_systems'),
    path('anti_theft_sensors_and_labels/', Anti_theft_sensors_and_labelsListAPIView.as_view(), name='anti_theft_sensors_and_labels'),
    path('key_pullers_and_deactivators/', Key_pullers_and_deactivatorsListAPIView.as_view(), name='key_pullers_and_deactivators'),
    path('ready_made_kits/', Ready_made_kitsListAPIView.as_view(), name='ready_made_kits'),
    path('visitor_counter/', Visitor_counterListAPIView.as_view(), name='visitor_counter'),
    path('shelving_protection/', Shelving_protectionListAPIView.as_view(), name='shelving_protection'),
    path('electronic_shelf_labels/', Electronic_shelf_labelsListAPIView.as_view(), name='electronic_shelf_labels'),
    path('digital_automation/', Digital_automationListAPIView.as_view(), name='digital_automation'),
    path('customers/', CustomersListAPIView.as_view(), name='customers'),
    path('anti_theft_systems/<str:id>/', Anti_theft_systemsDetailAPIView.as_view(), name='anti_theft_systems_detail'),
    path('anti_theft_sensors_and_labels/<str:id>/', Anti_theft_sensors_and_labelsDetailAPIView.as_view(), name='anti_theft_sensors_and_labels_detail'),
    path('key_pullers_and_deactivators/<str:id>/', Key_pullers_and_deactivatorsDetailAPIView.as_view(), name='key_pullers_and_deactivators_detail'),
    path('ready_made_kits/<str:id>/', Ready_made_kitsDetailAPIView.as_view(), name='ready_made_kits_detail'),
    path('visitor_counter/<str:id>/', Visitor_counterDetailAPIView.as_view(), name='visitor_counter_detail'),
    path('shelving_protection/<str:id>/', Shelving_protectionDetailAPIView.as_view(), name='shelving_protection_detail'),
    path('electronic_shelf_labels/<str:id>/', Electronic_shelf_labelsDetailAPIView.as_view(), name='electronic_shelf_labels_detail'),
    path('digital_automation/<str:id>/', Digital_automationDetailAPIView.as_view(), name='digital_automation_detail'),
]
