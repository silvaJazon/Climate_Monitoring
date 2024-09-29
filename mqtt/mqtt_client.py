import paho.mqtt.client as mqtt
import json
import django
import os
import sys
import logging
from datetime import datetime

# Configurar o logging para enviar logs para o journal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Adicionar o diretorio raiz do projeto ao sys.path
sys.path.append('/home/pi/Projetos/web_Server_Django/WebServer')

# Configurar as variaveis de ambiente para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebServer.settings')
django.setup()

# Importar modelos corretamente
from SensorData.models import SHTData, BMPData, Device

def on_message(client, userdata, message):
    try:
        # Converter a carga util da mensagem para JSON
        payload = json.loads(message.payload.decode('utf-8'))
        
        # Obter o timestamp atual
        timestamp = datetime.now()
        
        # Obter ou criar o Device correspondente
        device_id = payload['Device']['ID']
        device_data, created = Device.objects.get_or_create(
            id=device_id,
            defaults={
                'sht_ativo': payload['Device']['SHT_Ativo'],
                'bmp_ativo': payload['Device']['BMP_Ativo']
            }
        )

        # Criar e salvar instancias de SHTData e BMPData
        sht_data = SHTData(
            temp=payload['SHT']['Temp'],
            umid=payload['SHT']['Umid'],
            falha=payload['SHT']['Falha'],
            a_temp=payload['SHT']['A_Temp'],
            a_umid=payload['SHT']['A_Umid'],
            timestamp=timestamp,
            device=device_data
        )
        sht_data.save()
        logger.info(f"SHTData salvo com sucesso: {sht_data}")

        bmp_data = BMPData(
            temp=payload['BMP']['Temp'],
            press=payload['BMP']['Press'],
            falha=payload['BMP']['Falha'],
            timestamp=timestamp,
            device=device_data
        )
        bmp_data.save()
        logger.info(f"BMPData salvo com sucesso: {bmp_data}")

        logger.info(f"Mensagem recebida no topico {message.topic}: {payload}")
    except Exception as e:
        logger.error(f"Erro ao processar a mensagem: {e}")

def run_mqtt_client():
    # Configurar o cliente MQTT
    client = mqtt.Client()

    # Definir as funcoes de callback
    client.on_message = on_message

    # Conectar ao broker Mosquitto
    client.connect("localhost", 1883, 60)  # Substitua 'localhost' pelo endereco do seu broker se necessario

    # Subscrever aos topicos desejados
    client.subscribe("sensores")

    # Iniciar o loop do cliente MQTT para escutar as mensagens
    client.loop_forever()

if __name__ == "__main__":
    run_mqtt_client()
