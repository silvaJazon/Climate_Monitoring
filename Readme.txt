Recaregar Sytemd:
sudo systemctl daemon-reload

Caminho:
sudo nano /etc/systemd/system/django.service
sudo nano /etc/systemd/system/mqtt_client.service

Enable Sevice:
sudo systemctl enable django.service
sudo systemctl enable mqtt_client.service

Start Service:
sudo systemctl start django.service
sudo systemctl start mqtt_client.service

Status Service:
sudo systemctl status django.service
sudo systemctl status mqtt_client.service

Stop Service:
sudo systemctl stop django.service
sudo systemctl stop mqtt_client.service

Desativar Service:
sudo systemctl disable django.service
sudo systemctl disable mqtt_client.service

Reiniciar Service:
sudo systemctl restart django.service
sudo systemctl restart mqtt_client.service

journalctl services:
sudo journalctl -u django.service -f
sudo journalctl -u mqtt_client.service -f
