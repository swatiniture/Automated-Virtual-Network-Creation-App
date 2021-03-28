def create_sg(neutron):
    try:
        print('\n******** Adding ingress rules to allow ICMP and TCP to default SG ********\n')
        neutron.format = 'json'
        request1 = {
            'security_group_rule': {
                'security_group_id': 'f82659b1-8661-41f8-b3b8-1d9e1ae6e1aa',
                'protocol': 'icmp',
                'remote_ip_prefix': '172.24.4.0/24',
                'direction': 'ingress'
            }
        }
        request2 = {
            'security_group_rule': {
                'security_group_id': 'f82659b1-8661-41f8-b3b8-1d9e1ae6e1aa',
                'protocol': 'tcp',
                'remote_ip_prefix': '172.24.4.0/24',
                'direction': 'ingress'
            }
        }
        neutron.create_security_group_rule(request1)
        print('Rule added to allow ICMP')
        neutron.create_security_group_rule(request2)
        print('Rule added to allow TCP')

        print('\n******** Done adding ingress rules to allow ICMP and TCP to default SG ********\n')

    except Exception as e:
        print('Exception occurred', e)


