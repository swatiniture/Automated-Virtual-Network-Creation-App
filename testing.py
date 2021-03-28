try:
    from netmiko import ConnectHandler
    from novaclient import client as novaclient
    import time
    import sys

    from keystoneauth1 import identity
    from keystoneauth1 import session
    from neutronclient.v2_0 import client
    from novaclient import client as novaclient

except Exception:
    print('Please install all the necessary modules')
    sys.exit()

username = 'admin'
password = 'secret'
project_name = 'lab8'
project_domain_id = 'default'
user_domain_id = 'default'
auth_url = 'http://172.16.201.0/identity'
auth = identity.Password(auth_url=auth_url,
                          username=username,
                          password=password,
                          project_name=project_name,
                          project_domain_id=project_domain_id,
                          user_domain_id=user_domain_id)
sess = session.Session(auth=auth)
neutron = client.Client(session=sess)


def test():
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

if __name__ == '__main__':
    test()
