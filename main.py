try:
    import network_creation
    import sg_creation
    import vm_creation
    import router_creation
    import fip_creation
    import frr
    import ryu
    import test

    import os
    import sys
    import time

    from keystoneauth1 import identity
    from keystoneauth1 import session
    from neutronclient.v2_0 import client
    from novaclient import client as novaclient
    from netmiko import ConnectHandler

except Exception as e:
    print('Please install all the necessary modules', e)
    sys.exit()


auth = identity.Password(username='admin',
                         password='secret',
                         project_name='lab8',
                         auth_url='http://172.16.201.0/identity',
                         project_domain_id='default',
                         user_domain_id='default')
sess = session.Session(auth=auth)
neutron = client.Client(session=sess)

nova = novaclient.Client(version=2.1,
                         username='admin',
                         password='secret',
                         project_name='lab8',
                         auth_url='http://172.16.201.0/identity',
                         user_domain_id='default',
                         user_domain_name='default',
                         project_domain_name='default')

if __name__ == '__main__':
    network_creation.create_network(neutron)
    sg_creation.create_sg(neutron)
    vm_creation.create_new_vm(nova)
    router_creation.create_router(neutron, nova)
    fip_creation.create_fip(neutron, nova)
    ryu.push_conf_ryu(os, time)
    frr.push_conf_frr(os, time)
    test.test_connectivity(neutron)
