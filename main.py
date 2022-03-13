from netmiko import SSHDetect
from netmiko import ConnectHandler
import yaml


with open("creds.yaml") as _fp:
    creds = yaml.safe_load(_fp.read())
    username = creds["username"]
    password = creds["password"]

with open("routerips.txt") as ips:
    for ip in ips:
        # This device spec does not include the driver we use to connect with (ios or similar)
        # because we dont know it yet. The usual key for this value is "device_type"
        remote_device = {
            "device_type": "autodetect",
            "ip": ip,
            "username": username,
            "password": password,
        }
        # SSHDetect object is created
        guesser = SSHDetect(**remote_device)
        # Call method autodetect and get a string back: The driver most likely for this session
        best_match = guesser.autodetect()
        print(f"best_match = {best_match}")

        # We take the previously defined device spec and update the device_type now that we know
        # the most likely driver
        remote_device["device_type"] = best_match
        # Then we build a standard SSH connection
        connection = ConnectHandler(**remote_device)

        # Dependant on the driver, we get to work
        if best_match in ["cisco_ios", "cisco_xr"]:
            connection.enable()
            cli_show_clock = connection.send_command("show clock")
            print(cli_show_clock)

        if best_match in ["juniper_junos"]:
            connection.enable()
            cli_show_clock = connection.send_command("show system uptime | match 'Current time: '")
            print(cli_show_clock)