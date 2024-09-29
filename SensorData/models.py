from django.db import models

class Device(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True, blank=True)
    sht_ativo = models.BooleanField(null=True, blank=True)
    bmp_ativo = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return str(f'{self.id}')
     
    class Meta:
        verbose_name = '1 - Dispositivo'
        verbose_name_plural = '1 - Dispositivos'

class SHTData(models.Model):
    temp = models.FloatField(null=True, blank=True, verbose_name='Temperatura')
    umid = models.FloatField(null=True, blank=True, verbose_name='Umidade')
    falha = models.BooleanField(null=True, blank=True)
    a_temp = models.BooleanField(null=True, blank=True, verbose_name='Alarme de Temperatura')
    a_umid = models.BooleanField(null=True, blank=True, verbose_name='Alarme de Umidade')
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True, related_name='sht_data')

    class Meta:
        verbose_name = '2 - Dados do Sensor SHT'
        verbose_name_plural = '2 - Dados dos Sensores SHT'
        
class BMPData(models.Model):
    temp = models.FloatField(null=True, blank=True, verbose_name='Temperatura')
    press = models.FloatField(null=True, blank=True, verbose_name='Pressao')
    falha = models.BooleanField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True, related_name='bmp_data')

    class Meta:
        verbose_name = '3 - Dados do Sensor BMP'
        verbose_name_plural = '3 - Dados dos Sensores BMP'
