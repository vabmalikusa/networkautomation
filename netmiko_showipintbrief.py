from netmiko import ConnectHandler
import getpass
pass123 = "cisco"
multi_devices123 = ["192.168.29.131", "192.168.29.132", "192.168.29.133", "192.168.29.134"]
for abc123 in multi_devices123:
    ciscodevices123 = {
        "device_type": "cisco_ios",
        "ip": abc123,
        "username": input("enter the username: " ),
        "password": pass123,
        }
    connection123 = ConnectHandler(**ciscodevices123)
    print("#" * 10 + " CONNECTING TO " + abc123 + "#" * 10)
    output123 = connection123.send_command("show ip int br")
    print(output123)
    print("#" * 10 + " DISCONECTED FROM " + abc123 + "#" * 10)
