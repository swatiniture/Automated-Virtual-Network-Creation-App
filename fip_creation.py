def create_fip(neutron, nova):
    try:
        print('\n******** Creating and associating Floating IPs ********\n')
        list_vm_ids = []
        list_vms = []
        mapping = {}
        a = nova.servers.list()
        for server in a:
            list_vm_ids.append(server.id)
            list_vms.append(server.name)
        port_list = neutron.list_ports()
        list_port_ids = []
        for i in port_list['ports']:
            if i['device_id'] in list_vm_ids:
                list_port_ids.append(i['id'])
                mapping[(i['device_id'])] = i['id']
                
        neutron.format = 'json'
        
        for vm, port_id in mapping.items():
            request = {
                'floatingip': {
                    'port_id': port_id,
                    'floating_network_id': 'dd3ed010-1506-46cf-a8cf-be8a60eecf6b'
                }
            }
            neutron.create_floatingip(request)
            print('Associated Floating IP for Instance {}'.format(vm))

        print('\n******** Done creating and associating Floating IPs ********\n')

    except Exception as e:
        print('Exception occurred', e)




