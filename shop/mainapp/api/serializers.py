from rest_framework import serializers

from ..models import *

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]

class BaseProductSerializer:

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(required=True)

class Anti_theft_systemsSerializer(BaseProductSerializer, serializers.ModelSerializer):

    technology = serializers.CharField(required=True)
    sensor_detection_distance = serializers.CharField(required=True)
    tag_detection_distance = serializers.CharField(required=True)
    operating_frequency = serializers.CharField(required=True)
    alarm_indication = serializers.CharField(required=True)

    class Meta:
        model = Anti_theft_systems
        fields = '__all__'

class Anti_theft_sensors_and_labelsSerializer(BaseProductSerializer, serializers.ModelSerializer):

    type = serializers.CharField(required=True)
    technology = serializers.CharField(required=True)
    operating_frequency = serializers.CharField(required=True)

    class Meta:
        model = Anti_theft_sensors_and_labels
        fields = '__all__'


class Key_pullers_and_deactivatorsSerializer(BaseProductSerializer, serializers.ModelSerializer):

    class Meta:
        model = Key_pullers_and_deactivators
        fields = '__all__'


class Ready_made_kitsSerializer(BaseProductSerializer, serializers.ModelSerializer):

    main_params = serializers.CharField(required=True)
    equipment = serializers.CharField(required=True)

    class Meta:
        model = Ready_made_kits
        fields = '__all__'


class Visitor_counterSerializer(BaseProductSerializer, serializers.ModelSerializer):

    weight = serializers.CharField(required=True)
    dimensions = serializers.CharField(required=True)
    counting_zone = serializers.CharField(required=True)
    audible_indication_of_overlaps = serializers.CharField(required=True)
    monitoring_of_emergency_situations = serializers.CharField(required=True)
    power = serializers.CharField(required=True)
    device_memory = serializers.CharField(required=True)
    counting_mode = serializers.CharField(required=True)
    light_indication_of_passages = serializers.CharField(required=True)
    setting_up_method = serializers.CharField(required=True)
    data_transfer_method = serializers.CharField(required=True)
    data_storage = serializers.CharField(required=True)
    warranty = serializers.CharField(required=True)
    manufacturer = serializers.CharField(required=True)

    class Meta:
        model = Visitor_counter
        fields = '__all__'


class Shelving_protectionSerializer(BaseProductSerializer, serializers.ModelSerializer):

    interface = serializers.CharField(required=True)
    alarm_indication = serializers.CharField(required=True)
    manufacturer_country = serializers.CharField(required=True)

    class Meta:
        model = Shelving_protection
        fields = '__all__'

class Electronic_shelf_labelsSerializer(BaseProductSerializer, serializers.ModelSerializer):

    class Meta:
        model = Electronic_shelf_labels
        fields = '__all__'

class Digital_automationSerializer(BaseProductSerializer, serializers.ModelSerializer):

    class Meta:
        model = Digital_automation
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'