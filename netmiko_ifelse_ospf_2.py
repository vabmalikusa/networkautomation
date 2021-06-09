from netmiko import ConnectHandler
device123 = {
    "device_type": "cisco_ios",
    "ip": "192.168.29.131",
    "username": "admin",
    "password": "cisco",
}
ssh123 = ConnectHandler(**device123)
cmds = ["router ospf 100","network 0.0.0.0 0.0.0.0 area 0", "router-id 1.1.1.1"]
output123 = ssh123.send_config_set(cmds)
print(output123)
clear123 = ssh123.send_command_timing("clear ip ospf process")
print(clear123)
str_to_list123 = clear123.splitlines()[0]
print(str_to_list123)
if "Reset" in str_to_list123:
        ssh123.write_channel("yes")
        ssh123.send_command("\n")
        print("LOADING to FULL, Loading DONE")
        new123 = ssh123.send_command("sh ip osp neighbor e0/0 detail | i up")
        print(new123)
else:
    print("OSPF NOT CONFIGURED")
