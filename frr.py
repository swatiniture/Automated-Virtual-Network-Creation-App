def push_conf_frr(os, time):
    print('\n******** Before FRR image pull ********\n')
    os.system('docker images')
    os.system('docker pull frrouting/frr-debian')
    print('\n******** After FRR image pull ********\n')
    os.system('docker images')

    os.system('docker run -tid --name quagga1 frrouting/frr-debian /bin/bash')
    print('\n******** Running containers ********\n')
    os.system('docker ps -a')

    print('\n******** Copying python file to container quagga1 to change daemons file ********\n')
    os.system('docker cp change_daemons_file.py quagga1:/')

    print('\n******** Changing daemons file ********\n')
    os.system('docker exec -it  quagga1 python3 change_daemons_file.py')

    print('\n******** Committing new image ********\n')
    os.system('docker commit quagga1 quagga/new')

    print('\n******** Running new container with new image and copying configs for BGP ********\n')
    os.system('docker run -v /opt/stack/devstack/nvo_lav8_main/my_frr_conf:/etc/frr/frr.conf -itd --privileged --name quagga_new quagga/new')

    time.sleep(5)

    print('\n******** Running containers ********\n')
    os.system('docker ps -a')

    print('\n******** Checking BGP neighbors ********\n')
    out1 = os.popen('docker exec -it quagga_new vtysh -c "sh ip bgp neighbors"').read()
    print(out1)
    out2 = os.popen('docker exec -it quagga_new vtysh -c "sh ip bgp summary"').read()
    print(out2)




