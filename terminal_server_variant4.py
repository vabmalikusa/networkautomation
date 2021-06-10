 from netmiko import ConnectHandler, redispatch
import logging
import time
logging.basicConfig(filename='netmiko_global.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
device123 = {
    "device_type": "terminal_server",
    "ip": "192.168.29.141",
    "username": "network-automation",
    "password": "cisco",
}
ssh123 = ConnectHandler(**device123)
output123 = ssh123.send_command("ifconfig")
print(output123)
#cisco
ip123 = [" 192.168.29.133"]
for xyz123 in ip123:
    usernamer123 = "admin"
    ssh123.write_channel("ssh -l " + usernamer123 + xyz123 + "\n")
    max_trial = 4
    i = 1
    while i <= max_trial:
        ssh123.write_channel(input("enter the password for ") + "\n")
        time.sleep(1)
        output345 = ssh123.read_channel()
        if ">" in output345 or "#" in output345:
            break
        i += 1
    redispatch(ssh123, device_type="cisco_ios")
    output124 = ssh123.send_config_set("logging host 2.2.2.2")
    print(output124)
*redispatch used for changing device_type
