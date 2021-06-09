from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException
multiple_devices = open("D:\\customerxyz\\alldevices.txt")
for xyz123 in multiple_devices:
    xyz123 = xyz123.strip()
    devices123 = {
        "device_type": "cisco_ios",
        "host": xyz123,
        "username": "admin",
        "password": "cisco",
        "secret": "cisco123"
    }
    try:
        ssh123 = ConnectHandler(**devices123)
    except  NetmikoTimeoutException:
        print("DEVICE IP NOT FOUND " + xyz123 + "NetmikoTimeoutException")
        continue
    except NetmikoAuthenticationException:
        print("DEVICE USER/PASS DO NOT MATCH " + xyz123)
        continue
    output123 = ssh123.send_command("sh ip int br")
    print(output123)
