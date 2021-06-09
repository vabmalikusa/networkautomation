from netmiko import ConnectHandler
multiple_devices = open("D:\\customerxyz\\alldevices.txt")
for xyz123 in multiple_devices:
    xyz123 = xyz123.strip()
    devices123 = {
        "device_type": "cisco_ios",
        "host": xyz123,
        "username": "admin",#priv15
        "password": "cisco",
    }
    ssh123 = ConnectHandler(**devices123)
    #ssh open
    print("SUCCESSFUL CONNECTION TO >> " + xyz123  + "#" * 15)
    multiple_cli = ["show clock", " show ip int br"]
    a123 = ssh123.find_prompt()
    a123 = a123.rstrip("#")
    print(a123)
    from datetime import datetime
    now123 = datetime.now()
    #print(now123)
    new_now123 = str(now123.year) + "-" + str(now123.month) + "-" + str(now123.day)
    print(new_now123)
    for abc123 in multiple_cli:
        config123 = ssh123.send_command(abc123)
        #saving of backup
        filepath123 = "D:\\customerxyz\\CR12345678\\backup_"
        opennewblankfile = open(filepath123 + "collection_logs" + "-" + a123 + "_" + new_now123 + ".log", "a")
        opennewblankfile.write("\n" + 5 * "#" + abc123 + "\n")
        opennewblankfile.write(config123)
        opennewblankfile.close()
        print(config123)
    print("DISCONNECTING FROM >> " + xyz123 + "#" * 15)
