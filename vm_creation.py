def create_new_vm(nova):
    try:
        print('\n******** Creating Instances ********\n')
        image = nova.glance.find_image('ngn-qcow')
        flavor = nova.flavors.find(name='ngn.tiny')
        networks = {'net1': ['vm11', 'vm12'], 'net2': ['vm21', 'vm22']}
        for net, vms in networks.items():
            for vm in vms:
                network = nova.neutron.find_network(name=net).id
                instance = vm
                nova.servers.create(name=instance, flavor=flavor, image=image, nics=[{'net-id':network}])
                print('New Instance {} is created in network {}'.format(instance, net))

        print('\n******** Done creating Instances ********\n')

    except Exception as e:
        print('Exception occurred', e)
