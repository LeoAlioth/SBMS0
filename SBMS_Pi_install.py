import os
import socket

os.system("apt update")
os.system("apt upgrade -y")

# Install & configure InfluxDB
os.system("wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -")
os.system("'deb https://repos.influxdata.com/debian bullseye stable' | sudo tee /etc/apt/sources.list.d/influxdb.list")
os.system("apt update")
os.system("apt install influxdb")
os.system("systemctl unmask influxdb")
os.system("systemctl enable influxdb")
os.system("systemctl start influxdb")
os.system("sudo apt install influxdb-client")
os.system("influx -execute 'CREATE DATABASE SBMS'")

os.system("sudo apt-get install python3-pip")
os.system("pip3 install pyserial")
os.system("pip3 install pip install influxdb")

# Install Grafana
os.system("apt-get install -y adduser libfontconfig1")
# Package for Intel based install
#os.system("wget https://dl.grafana.com/oss/release/grafana_7.1.1_amd64.deb")
#os.system("sudo dpkg -i grafana_7.1.1_amd64.deb")

os.system("wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -")
os.system("echo 'deb https://packages.grafana.com/oss/deb stable main' | sudo tee -a /etc/apt/sources.list.d/grafana.list")
os.system("apt update")
os.system("apt install -y grafana")
os.system("systemctl enable grafana-server")
os.system("systemctl start grafana-server")

os.system("sudo wget --no-check-certificate --content-disposition 'https://raw.githubusercontent.com/LeoAlioth/SBMS0/master/sbms0-SerialToInfluxDB.py' -P '/home/SBMS0/'")

os.system("sudo wget --no-check-certificate --content-disposition 'https://raw.githubusercontent.com/LeoAlioth/SBMS0/master/SBMS-Logger.service' -P '/etc/systemd/system/'")

os.system("systemctl enable SBMS-Logger.service")
os.system("systemctl start SBMS-Logger.service")

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ipaddress = get_ip_address()
os.system("curl --user admin:admin \"http://" + ipaddress + ":3000/api/datasources\" -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{\"name\":\"SBMS_Data\",\"isDefault\":true ,\"type\":\"influxdb\",\"url\":\"http://localhost:8086\",\"database\":\"SBMS\",\"access\":\"proxy\",\"basicAuth\":false}'")

print("Login to http://" + ipaddress + ":3000")
print("Username = admin, password = admin")
