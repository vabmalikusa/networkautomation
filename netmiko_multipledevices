from netmiko import ConnectHandler
import logging
logging.basicConfig(filename="packetinspection123.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")
#
pass123 = "cisco"
multi_devices123 = ["192.168.29.131", "192.168.29.132", "192.168.29.133"]
for abc123 in multi_devices123:
    ciscodevices123 = {
        "device_type": "cisco_ios",
        "ip": abc123,
        "username": "admin",
        "password": pass123,
        }
    connection123 = ConnectHandler(**ciscodevices123)
    print("#" * 10 + " CONNECTING TO " + abc123 + "#" * 10)
    output123 = connection123.send_commmand("show clock")
    output345 = connection123.send_command("show ip int br")
    output346 = connection123.send_command("show ver")
    print("show clock")
    print(output123)
    print("show ip int br")
    print(output345)
    print("show version")
    print(output346)
    print("#" * 10 + " DISCONNECTED FROM " + abc123 + "#" * 10)
