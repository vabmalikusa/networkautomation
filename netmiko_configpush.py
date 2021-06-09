from netmiko import ConnectHandler
multiple_devices = open("config.txt")
for xyz123 in multiple_devices:
    devices123 = {
        "device_type": "cisco_ios",
        "host": xyz123,
        "username": "admin",#priv15
        "password": "cisco",
    }
    ssh123 = ConnectHandler(**devices123)
    #ssh open
    hostname = ssh123.find_prompt()
    #print(hostname)
    print("SUCCESSFUL CONNECTION TO >> " + xyz123 + hostname + "#" * 15)
    userdefined123 = input("enter the config you want to push:")
    config123 = ssh123.send_config_from_file(userdefined123)
    print(config123)
    print("DISCONNECTING FROM >> " + xyz123 + "#" * 15)
    ssh123.disconnect()
