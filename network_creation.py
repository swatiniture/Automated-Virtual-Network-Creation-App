def create_network(neutron):
    try:
        print('\n******** Creating Networks and Subnets ********\n')
        networks = {'net1': '10.10.10.0/24', 'net2': '20.20.20.0/24'}
        
        for network, ip in networks.items():
            data = {'network': {'name': network, 'admin_state_up': True}}
            netw = neutron.create_network(body=data)
            network_id = netw['network']['id']
            print('Network {} with ID {} is created'.format(network, network_id))
            body_create_subnet = {'subnets': [{'name': 'sub' + network, 'cidr': ip,
                                               'ip_version': 4, 'network_id': network_id}]}

            subnet = neutron.create_subnet(body=body_create_subnet)
            subnet_id = subnet['subnets'][0]['id']
            print('Subnet sub{} with ID {} is created'.format(network, subnet_id))

        print('\n******** Done creating Networks and Subnets ********\n')

    except Exception as e:
        print('Exception occurred', e)

