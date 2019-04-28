from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.common.client_factory import get_client_from_cli_profile
from functools import lru_cache
from typing import Dict
import json
import os


# Load global config
with open('config.json', 'r') as f:
    CONFIG = json.load(f)

TENANT_ID = CONFIG['GLOBAL']['TENANT_ID']
LOCATION = CONFIG['GLOBAL']['LOCATION']

# Other global definitions
RESOURCE_CACHE_FILENAME = '.resources_cache.json'

class AzResourceManager:

    def __init__(self):
        self.resource_client = get_client_from_cli_profile(ResourceManagementClient)
        self.network_client = get_client_from_cli_profile(NetworkManagementClient)
        self.compute_client = get_client_from_cli_profile(ComputeManagementClient)
        self.resource_groups = []
        self.resources = {}

    @lru_cache(maxsize=32)
    def load_resources(self):
        if os.path.isfile(RESOURCE_CACHE_FILENAME):
            print ("Loading resources from cache...")
            self.load_resources_from_file()
            return

        print ("Fetching resource from Azure Resource Manager...")
        for resource_group in self.resource_client.resource_groups.list():
            self.resource_groups.append(resource_group.name)

        for rg in self.resource_groups:
            self.resources[rg] = []
            for resource in self.resource_client.resources.list_by_resource_group(rg):
                self.resources[rg].append(resource.as_dict())
        
        with open(RESOURCE_CACHE_FILENAME, 'w') as f:
            json.dump(self.resources, f)

    def load_resources_from_file(self):
        with open(RESOURCE_CACHE_FILENAME, 'r') as f:
            self.resources = json.load(f)
        
        for resource_group in self.resources.keys():
            self.resource_groups.append(resource_group)


    @lru_cache(maxsize=32)
    def get_public_ip_addresses(self):
        pips = []
        for rg in self.resource_groups:
            for resource in self.resources[rg]:
                if "publicIPAddresses" in resource['type']:
                    pip_name = resource['name']
                    pip_addr = self.network_client.public_ip_addresses.get(rg, pip_name).ip_address
                    if pip_addr is not None:
                        pip_dict_entry = {
                            'name': pip_name,
                            'ip_address': pip_addr
                        }
                        pips.append(pip_dict_entry)
        return pips

if __name__ == '__main__':
    print ("Starting...")
    arm = AzResourceManager()

    arm.load_resources()
    #res_dict = arm.resources

    menu = {}
    menu['1']="Get public IP addresses" 
    menu['2']="Exit"
    
    while True: 
        options = sorted(menu.keys())
        #options.sort()
        for entry in options: 
            print (entry, menu[entry])

        selection=input("\nPlease Select: ")
        if selection =='1':
            print("Getting all public IP addresses" )
            pips = arm.get_public_ip_addresses()
            for pip in pips:
                print ("{}: {}".format(pip['name'], pip['ip_address']))
        elif selection == '2':
            break
        else:
            print("Invalid Option!")

    


## arm.network_client.network_security_groups.get('GOE-HUB-NPR-SEC-rg','GOE-NPR-ManagementSubnet-nsg').as_dict().security_rules

