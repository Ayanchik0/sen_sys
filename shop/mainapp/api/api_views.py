from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from ..models import *


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):

        return Response(OrderedDict([
            ('objects.count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()


class CustomersListAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class Anti_theft_systemsListAPIView(ListAPIView):

    serializer_class = Anti_theft_systemsSerializer
    queryset = Anti_theft_systems.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Anti_theft_systemsDetailAPIView(RetrieveAPIView):

    serializer_class = Anti_theft_systemsSerializer
    queryset = Anti_theft_systems.objects.all()
    lookup_field = 'id'


class Anti_theft_sensors_and_labelsListAPIView(ListAPIView):

    serializer_class = Anti_theft_sensors_and_labelsSerializer
    queryset = Anti_theft_sensors_and_labels.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Anti_theft_sensors_and_labelsDetailAPIView(RetrieveAPIView):

    serializer_class = Anti_theft_sensors_and_labelsSerializer
    queryset = Anti_theft_sensors_and_labels.objects.all()
    lookup_field = 'id'


class Key_pullers_and_deactivatorsListAPIView(ListAPIView):

    serializer_class = Key_pullers_and_deactivatorsSerializer
    queryset = Key_pullers_and_deactivators.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Key_pullers_and_deactivatorsDetailAPIView(RetrieveAPIView):

    serializer_class = Key_pullers_and_deactivatorsSerializer
    queryset = Key_pullers_and_deactivators.objects.all()
    lookup_field = 'id'


class Ready_made_kitsListAPIView(ListAPIView):

    serializer_class = Ready_made_kitsSerializer
    queryset = Ready_made_kits.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Ready_made_kitsDetailAPIView(RetrieveAPIView):

    serializer_class = Ready_made_kitsSerializer
    queryset = Ready_made_kits.objects.all()
    lookup_field = 'id'


class Visitor_counterListAPIView(ListAPIView):

    serializer_class = Visitor_counterSerializer
    queryset = Visitor_counter.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Visitor_counterDetailAPIView(RetrieveAPIView):

    serializer_class = Visitor_counterSerializer
    queryset = Visitor_counter.objects.all()
    lookup_field = 'id'


class Shelving_protectionListAPIView(ListAPIView):

    serializer_class = Shelving_protectionSerializer
    queryset = Shelving_protection.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Shelving_protectionDetailAPIView(RetrieveAPIView):

    serializer_class = Shelving_protectionSerializer
    queryset = Shelving_protection.objects.all()
    lookup_field = 'id'


class Electronic_shelf_labelsListAPIView(ListAPIView):

    serializer_class = Electronic_shelf_labelsSerializer
    queryset = Electronic_shelf_labels.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Electronic_shelf_labelsDetailAPIView(RetrieveAPIView):

    serializer_class = Electronic_shelf_labelsSerializer
    queryset = Electronic_shelf_labels.objects.all()
    lookup_field = 'id'


class Digital_automationListAPIView(ListAPIView):

    serializer_class = Digital_automationSerializer
    queryset = Digital_automation.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class Digital_automationDetailAPIView(RetrieveAPIView):

    serializer_class = Digital_automationSerializer
    queryset = Digital_automation.objects.all()
    lookup_field = 'id'