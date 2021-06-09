from netmiko import ConnectHandler
DEV123 = {
    "device_type": "cisco_ios",
    "ip": "192.168.29.131",
    "username": "tom123",
    "password": "cisco",
    "port": 22,
    "secret": "cisco123",
}
ssh123 = ConnectHandler(**DEV123)
ssh123.enable()
output123 = ssh123.send_command("show run")
print(output123)
