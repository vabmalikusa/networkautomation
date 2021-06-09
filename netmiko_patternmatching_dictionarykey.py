from netmiko import ConnectHandler
multiple_devices = open("D:\\customerxyz\\alldevices.txt")
import logging
logging.basicConfig(filename='test-netmiko-priv.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
for xyz123 in multiple_devices:
    xyz123 = xyz123.strip()
    devices123 = {
        "device_type": "cisco_ios",
        "host": xyz123,
        "username": "TIM",#priv5
        "password": "cisco",
        "secret": "cisco123"
    }
    ssh123 = ConnectHandler(**devices123)
    #ssh open
    ssh123.write_channel("enable\n")
    ssh123.read_until_prompt_or_pattern(pattern="Password:")
    ssh123.write_channel(devices123["secret"]\n")
    print('ENTERED PRI 15')
    print("SUCCESSFUL CONNECTION TO >> " + xyz123  + "#" * 15)
    output123 = ssh123.send_command("sh run")
    print(output123)
