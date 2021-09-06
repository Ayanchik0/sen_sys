from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import  ContentType
from django.contrib.contenttypes.fields import  GenericForeignKey
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        print(products)
        return products


class LatestProducts:

    objects = LatestProductsManager()



class CategoryManager(models.Manager):


    CATEGORY_NAME_COUNT_NAME = {
        'Противокражные системы': 'anti_theft_systems__count',
        'Противокражные датчики и этикетки': 'anti_theft_sensors_and_labels__count',
        'Ключ-съемники и деактиваторы': 'key_pullers_and_deactivators__count',
        'Готовые комплекты': 'ready_made_kits__count',
        'Счетчик числа посетителей': 'visitor_counter__count',
        'Защита на стеллажах': 'shelving_protection__count',
        'Электронные ценники': 'electronic_shelf_labels__count',
        'Цифровая автоматизация': 'digital_automation__count'
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):


        models = get_models_for_count('anti_theft_systems', 'anti_theft_sensors_and_labels', 'key_pullers_and_deactivators',
                                      'ready_made_kits', 'visitor_counter', 'shelving_protection', 'electronic_shelf_labels',
                                      'digital_automation')

        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()


class Anti_theft_systems(Product):

    technology = models.CharField(max_length=255, verbose_name='Технология')
    sensor_detection_distance = models.CharField(max_length=255, verbose_name='Расстояние детекции датчиков')
    tag_detection_distance = models.CharField(max_length=255, verbose_name='Расстояние детекции меток')
    operating_frequency = models.CharField(max_length=255, verbose_name='Рабочая частота')
    alarm_indication = models.CharField(max_length=255, verbose_name='Индикация тревоги')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Anti_theft_sensors_and_labels(Product):

    type = models.CharField(max_length=255, verbose_name='Тип')
    technology = models.CharField(max_length=255, verbose_name='Технология')
    operating_frequency = models.CharField(max_length=255, verbose_name='Рабочая частота')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Key_pullers_and_deactivators(Product):

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Ready_made_kits(Product):

    main_params = models.CharField(max_length=1000, verbose_name='Основные')
    equipment = models.CharField(max_length=1000, verbose_name='Комплектация')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Visitor_counter (Product):

    weight = models.CharField(max_length=255, verbose_name='Вес')
    dimensions = models.CharField(max_length=255, verbose_name='Габариты')
    counting_zone = models.CharField(max_length=255, verbose_name='Зона подсчета')
    audible_indication_of_overlaps = models.CharField(max_length=255, verbose_name='Звуковая индикация перекрытий')
    monitoring_of_emergency_situations = models.CharField(max_length=255, verbose_name='Контроль внештатных ситуаций')
    power = models.CharField(max_length=255, verbose_name='Питание')
    device_memory = models.CharField(max_length=255, verbose_name='Память устройства')
    counting_mode = models.CharField(max_length=255, verbose_name='Режим подсчета')
    light_indication_of_passages = models.CharField(max_length=255, verbose_name='Световая индикация проходов')
    setting_up_method = models.CharField(max_length=255, verbose_name='Способ настройки')
    data_transfer_method = models.CharField(max_length=255, verbose_name='Способ передачи данных')
    data_storage = models.CharField(max_length=255, verbose_name='Хранение данных')
    warranty = models.CharField(max_length=255, verbose_name='Гарантия и сервисное обслуживание')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Shelving_protection(Product):

    interface = models.CharField(max_length=255, verbose_name='Интерфейс')
    alarm_indication = models.CharField(max_length=255, verbose_name='Индикация тревоги')
    manufacturer_country = models.CharField(max_length=255, verbose_name='Страна производитель')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Electronic_shelf_labels(Product):

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Digital_automation(Product):

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

class Cart(models.Model):


    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')

    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'


    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )


    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )

    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)
