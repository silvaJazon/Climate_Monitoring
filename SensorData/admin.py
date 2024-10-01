from django.contrib import admin
from .models import SHTData, BMPData, Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sht_ativo', 'bmp_ativo')
    search_fields = ('id',)
   

@admin.register(SHTData)
class SHTDataAdmin(admin.ModelAdmin):
    list_display = ('device','temp', 'umid', 'falha', 'a_temp', 'a_umid', 'timestamp')
    search_fields = ('device','temp', 'umid')

@admin.register(BMPData)
class BMPDataAdmin(admin.ModelAdmin):
    list_display = ('device','temp', 'press', 'falha', 'timestamp')
    search_fields = ('device','temp', 'press')


