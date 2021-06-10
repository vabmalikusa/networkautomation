from netmiko import ConnectHandler
import logging
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
    usernamer123 = input("Enter the username for " + xyz123 + ":")
    ssh123.write_channel("ssh -l " + usernamer123 + xyz123 + "\n")
    output123 = ssh123._read_channel_expect()
    if "Password" or "password" or "login" in output123:
        ssh123.write_channel(input("enter the password for ") + "\n")
        output124 = ssh123.send_command("show ip int br")
        print(output124)
