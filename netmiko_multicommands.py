from netmiko import ConnectHandler
import logging
logging.basicConfig(filename="packetinspection23453.log", level=logging.DEBUG)
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
    multi_commands = ["show clock",
                      "show ip int br",
                      "show ver",
                      "show version"]
    for ert123 in multi_commands:
        output123 = connection123.send_command(ert123)
        print(output123)
    print("#" * 10 + " DISCONNECTED FROM " + abc123 + "$" * 10)
