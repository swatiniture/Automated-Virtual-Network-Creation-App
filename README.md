# Automated-Virtual-Network-Creation-App

# What is it about

This repository provides an application for automated creation of virtual networks and BGP peering between FRR and RYU SDN controller.  

# Purpose

One-click python script enables end-to-end VM communication in OpenStack and formation of BGP peering between FRR and RYU SDN controller. This significantly reduces the time required to configure networks using command line.

# How to run?

Run the 'main.py' to run the application. The 'main.py' script imports all the remaining modules.

# Files 

1. network_creation.py: Creates two virtual networks and subnets
2. sg_creation.py: Adds the security rules to allow ingress ICMP and TCP traffic to the existing default security group
3. vm_creation.py: Spins up two instances in each network
4. router_creation.py: Adds a router to enable inter-VN communication, along with addition of gateway and ports in the networks created
5. fip_creation.py: Creates and associates floating IPs to instances for SSH connectivity and reachability to instances from external networks
6. ryu.py: Creates a RYU SDN docker container, adds a BGP config file to peer with FRR docker container (uses bgp_sample_conf.py)
7. frr.py: Creates an FRR docker container, makes changes in daemons file to enable BGP and adds a config file to peer with RYU SDN docker controller (uses change_daemons_file.py and my_frr_conf)

# Testing

The frr.py script shows the status of BGP peering relationship and test.py checks the SSH connectivity and reachability.




