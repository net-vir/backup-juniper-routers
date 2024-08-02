# import the required libraries
from netmiko import ConnectHandler
from datetime import datetime
import getpass

# Below code block is used to retrieve the device information/IPs from a text file
with open('Device-list') as f1:
    devices = f1.read().splitlines()

passwd = getpass.getpass("Enter the password: ")

# below for loop is used to re-iterate the below code for each line item/host in the device-list file
for hostip in devices:
    # below is a dictionary which defines the basic properties of a cisco device required for connection
    cisco_device = {
        'device_type': 'juniper',
        'host': hostip,
        'username': 'admin',
        'password': passwd,
        'port': 22,
    }
    connection = ConnectHandler(**cisco_device)
    output = connection.send_command('show configuration')

    prompt = connection.find_prompt()
    hostname = prompt[]

    #Below variables storing date and time information
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    #Below is a nice way of creating a new backup file with date and time information and reducing the chances of overwriting
    backup_file = f'{hostname}_{year}_{month}_{day}_{hour}_{minute}_{second}_Backup.txt'

    with open(backup_file, 'w') as f3:
        f3.writelines(all_outputs)

    connection.disconnect()
