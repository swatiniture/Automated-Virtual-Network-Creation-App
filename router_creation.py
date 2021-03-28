def create_router(neutron, nova):
    try:
        print('\n******** Creating Router and adding ports ********\n')
        public = nova.neutron.find_network(name='public').id
        # networks = neutron.list_networks(name='public')
        # network_id = networks['networks'][0]['id']

        neutron.format = 'json'
        request = {'router': {
            'name': 'lab8_router',
            'admin_state_up': True}
        }
        router = neutron.create_router(request)
        router_id = router['router']['id']
        router_name = router['router']['name']
        print('Created router {} with ID {}'.format(router_name, router_id))

        request2 = {
            'network_id': public}
        neutron.add_gateway_router(router_id, request2)

        print('Added public gateway to router {} with ID {}'.format(router_name, router_id))

        network1 = nova.neutron.find_network(name='net1').subnets[0]
        network2 = nova.neutron.find_network(name='net2').subnets[0]

        networks = {network1: 'p1', network2: 'p2'}
        # for network, port in networks.items():
        #     body_value = {'port': {
        #         'admin_state_up': True,
        #         'device_id': router_id,
        #         'name': port,
        #         'network_id': network,
        #         'security_groups': [],
        #         'port_security_enabled': False,
        #         'device_owner': 'network:router_gateway'
        #     }
        #     }
            # response = neutron.create_port(body=body_value)
            # print(response)
        for network, port in networks.items():
            body_value = {
                'name': port,
                'subnet_id': network,
            }
            neutron.add_interface_router(router_id, body_value)
            print('Added port {} to network {}'.format(port, network))

        print('\n******** Done creating Router and adding ports ********\n')

    except Exception as e:
        print('Exception occurred', e)
        
