# Trevor's clock script for checking the time on many Cisco/Juniper routers

In this script, you will need to create a creds.yaml which will look like the following

```
---
username: 'insert_username_here'
password: 'insert_password_here'
```

Make sure you keep the creds.yaml file in a secure location.

You will also need to create a file called routerips.txt and there you can dump your IP addresses for your routers that you want to verify the clock on. 