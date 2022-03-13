from netmiko import SSHDetect
from netmiko import ConnectHandler



username = 'REDACTED'
password = 'REDACTED'


with open('routerips.txt') as routers:
       for IP in routers:
             remote_device = {
                     'device_type': 'autodetect',
                     'ip' : IP,
                     'username': username,
                     'password': password
              }
       print(remote_device)
       

       guesser = SSHDetect(**remote_device)
       best_match = guesser.autodetect()
       print(guesser)

       remote_device['device_type'] = best_match
       print(best_match)

       if best_match != None:
              print("device_type: " + best_match)
       else:
              print("Device type not found!")
       break

       

       if remote_device['device_type'] == "juniper_junos":
              junos_routers = remote_device
              for IP in junos_routers:
                     junos_device = {
                            'device_type': remote_device['device_type'],
                            'ip': IP,
                            'username': username,
                            'password': password
                     }
              print('Connecting to ' + IP)
              with open('commands_junos.txt') as j:
                     lines_junos = j.read().splitlines()
                     print(lines_junos)
              for devices in remote_device:
                     net_connect = ConnectHandler(**remote_device)
                     for command in lines_junos:
                            output = net_connect.send_command(command)
              print(output)
       
       elif remote_device['device_type'] == ["cisco_ios", "cisco_xe", "cisco_xr"]:
              print('Connecting to ' + IP)
              with open('commands.txt') as f:
                     lines = j.read().splitlines()
                     print(lines)
              for devices in remote_device:
                     net_connect = ConnectHandler(**remote_device)
                     for command in lines:
                            output = net_connect.send_command(command)
              print(output)
       else:
              print("Device type not found")