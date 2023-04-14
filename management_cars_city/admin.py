from django.contrib import admin

from .models import Car, Person


class PersonAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'name', 'email')
    list_display = ('id', 'owner_car', 'name', 'lastname',
                    'email', 'cpf', 'cellphone')


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'color', 'owner_id')


admin.site.register(Person, PersonAdmin)
admin.site.register(Car, CarAdmin)
