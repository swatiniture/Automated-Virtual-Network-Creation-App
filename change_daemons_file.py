import re
import os

with open('/etc/frr/daemons', 'r+') as f:
    text = f.read()
    text = re.sub('(?<=bgpd=)(no)', 'yes', text)
    f.seek(0)
    f.write(text)
    f.truncate()

os.system('sysctl -w net.ipv4.ip_forward=1')
os.system('sysctl -w net.ipv6.conf.all.forwarding=1')
