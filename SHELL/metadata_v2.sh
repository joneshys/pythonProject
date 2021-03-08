#!/bin/bash
cd /home/ec2-user
sudo mkdir metadatav2 # Creación de la carpeta para alojar el update aws
cd metadatav2/
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" # Descarga del Update de la V2 AWS
sudo unzip awscliv2.zip # Descomprimir el archivo zip del Update de la V2 AWS
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update # Se realiza el update al AWS a la V2
sleep 5
InstancesID=`curl http://169.254.169.254/latest/meta-data/instance-id` # Se obtiene el id de la instancia
echo $InstancesID # Se obtiene el id de la instancia
aws ec2 modify-instance-metadata-options --instance-id $InstancesID --profile default --http-endpoint enabled --http-token required # Se habilita IMDSv2 en la maquina
