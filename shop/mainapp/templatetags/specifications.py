from django import template
from django.utils.safestring import mark_safe


register = template.Library()

TABLE_HEAD = """
                <table class="table table-striped table-hover">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'anti_theft_sensors_and_labels': {
        'Тип': 'type',
        'Технология': 'technology',
        'Рабочая частота': 'operating_frequency'
    },
    'anti_theft_systems': {

        'Технология': 'technology',
        'Расстояние детекции датчиков': 'sensor_detection_distance',
        'Расстояние детекции меток': 'tag_detection_distance',
        'Рабочая частота': 'operating_frequency',
        'Индикация тревоги': 'alarm_indication'
    },
    'digital_automation_specification': {
        'Рабочая частота': 'operating_frequency',
        'Питание': 'power'
    },
    'electronic_shelf_labels_specification': {
        'Размер': 'size'
    },
    'key_pullers_and_deactivators_specification': {
                'Тип': 'type',
        'Технология': 'technology',
    },
    'ready_made_kits': {
        'Основные': 'main_params',
        'Комплектация': 'equipment'
    },
    'visitor_counter': {
        'Вес': 'weight',
        'Габариты': 'dimensions',
        'Зона подсчета': 'counting_zone',
        'Звуковая индикация перекрытий': 'audible_indication_of_overlaps',
        'Контроль внештатных ситуаций': 'monitoring_of_emergency_situations',
        'Питание': 'power',
        'Память устройства': 'device_memory',
        'Режим подсчета': 'counting_mode',
        'Световая индикация проходов': 'light_indication_of_passages',
        'Способ настройки': 'setting_up_method',
        'Способ передачи данных': 'data_transfer_method',
        'Хранение данных': 'data_storage',
        'Гарантия и сервисное обслуживание': 'warranty',
        'Производитель': 'manufacturer'
    },
    'shelving_protection': {
        'Интерфейс': 'interface',
        'Индикация тревоги': 'alarm_indication',
        'Страна производитель': 'manufacturer_country'
    },
}

def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name

    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
