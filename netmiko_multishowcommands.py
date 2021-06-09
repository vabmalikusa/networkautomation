from netmiko import ConnectHandler
devices = ["192.168.29.131", "192.168.29.132", "192.168.29.149", "192.168.29.133",
            "192.168.29.135", "192.168.29.136", "192.168.29.137", "192.168.29.138"]
for xyz123 in devices:
    devices123 = {
        "device_type": "cisco_ios",
        "host": xyz123,
        "username": "admin",#priv15
        "password": "cisco",
    }
    ssh123 = ConnectHandler(**devices123)
    #ssh open
    print("SUCCESSFUL CONNECTION TO >> " + xyz123  + "#" * 15)
    multiple_cli = ["logging host 44.44.44.44", "logging host 44.44.44.45",
                        "logging host 44.44.44.46", "logging host 44.44.44.47",
                    "do show run | i logging", "do show clock", "do show ip int br"]
    config123 = ssh123.send_config_set(multiple_cli)
    print(config123)
    # multiple_show_command = ["show run | i logging", "show clock", "show ip int br"]
    # for abc123 in multiple_show_command:
    #     output123 = ssh123.send_command(abc123)
    #     print(output123)
    print("DISCONNECTING FROM >> " + xyz123 + "#" * 15)
