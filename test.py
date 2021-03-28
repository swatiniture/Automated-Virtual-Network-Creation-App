try:
    from netmiko import ConnectHandler
    import sys
except Exception:
    print('Please install all the necessary modules')
    sys.exit()

def test_connectivity(neutron):
    try:
        floating_ip_list = []
        for entry in neutron.list_floatingips()['floatingips']:
            floating_ip_list.append(entry['floating_ip_address'])
        print('\n******** Establishing SSH connection to the Cirros VM ********')
        device = {'device_type': 'linux', 'host': floating_ip_list[0], 'username': 'cirros', 'password': 'gocubsgo'}
        net_connect = ConnectHandler(**device)
        print('\n******** Established SSH connection to the Cirros VM ********')
        print('\n******** Checking hostname ********\n')
        out1 = net_connect.send_command('hostname')
        print(out1)
        print('\n******** pinging from above host to Internet and every other host********\n')
        out2 = net_connect.send_command('ping -c 2 8.8.8.8')
        print(out2)
        for i in range(1, len(floating_ip_list)):
            out = net_connect.send_command('ping -c 2 ' + floating_ip_list[i])
            print(out)

        net_connect.disconnect()
    except Exception as e:
        print(e)


