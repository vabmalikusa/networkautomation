from netmiko import ConnectHandler, file_transfer
devices123 = {
    "device_type": "cisco_ios",
    "host": "192.168.29.149",
    "username": "admin",
    "password": "cisco",
}
ssh123 = ConnectHandler(**devices123)
#ssh_console_open
output123 = file_transfer(ssh123, source_file="SW1.txt",
                          dest_file="SW1.txt", direction="put", file_system="flash0:",
                          overwrite_file=False, verify_file=False)
print(output123)
