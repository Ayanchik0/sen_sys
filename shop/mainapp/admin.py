from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class Anti_theft_systemsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='anti_theft_systems'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Anti_theft_sensors_and_labelsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='anti_theft_sensors_and_labels'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Key_pullers_and_deactivatorsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='key_pullers_and_deactivators'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Ready_made_kitsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='ready_made_kits'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Visitor_counterAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='visitor_counter'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Shelving_protectionAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shelving_protection'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Electronic_shelf_labelsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='electronic_shelf_labels'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class Digital_automationAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='digital_automation'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Anti_theft_systems, Anti_theft_systemsAdmin)
admin.site.register(Anti_theft_sensors_and_labels, Anti_theft_sensors_and_labelsAdmin)
admin.site.register(Key_pullers_and_deactivators, Key_pullers_and_deactivatorsAdmin)
admin.site.register(Ready_made_kits, Ready_made_kitsAdmin)
admin.site.register(Visitor_counter, Visitor_counterAdmin)
admin.site.register(Shelving_protection, Shelving_protectionAdmin)
admin.site.register(Electronic_shelf_labels, Electronic_shelf_labelsAdmin)
admin.site.register(Digital_automation, Digital_automationAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)