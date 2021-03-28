def push_conf_ryu(os, time):
    print('\n******** Before RYU image pull ********\n')
    os.system('docker images')
    os.system('docker pull osrg/ryu')
    print('\n******** After RYU image pull ********\n')
    os.system('docker images')

    os.system('sudo docker run -tid --name ryu osrg/ryu /bin/bash')
    print('\n******** Running containers ********\n')
    os.system('docker ps -a')

    print('\n******** Copying BGP conf python file to ryu container ********\n')
    os.system('docker cp bgp_sample_conf.py ryu:/root/ryu/ryu/services/protocols/bgp/conf_file')

    print('\n******** Updating packages on container and installing paramiko ********\n')
    os.system('docker exec -it ryu apt update -y')
    os.system('docker exec -it ryu apt install python-paramiko -y')

    print('\n******** Running the copied BGP conf file ********\n')
    os.system(
        'docker exec -d -it ryu ryu-manager /root/ryu/ryu/services/protocols/bgp/application.py --bgp-app-config-file  '
        '/root/ryu/ryu/services/protocols/bgp/conf_file')
    os.system('docker ps -a')
    
    time.sleep(5)

