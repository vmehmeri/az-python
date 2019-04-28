import json
from enum import Enum

with open('config.json', 'r') as f:
    CONFIG = json.load(f)

class Env(Enum):
    DEV = 1 
    TST = 2
    PRD = 3

class NetworkEnvironment:

    def __init__(self, name: Env):
        self.name = name.name
        self.subscription_name = CONFIG['SUBSCRIPTIONS'][self.name]['SUBSCRIPTION_NAME']
        self.subscription_id = CONFIG['SUBSCRIPTIONS'][self.name]['SUBSCRIPTION_ID']
        self.vnet_name = CONFIG['SUBSCRIPTIONS'][self.name]['VIRTUAL_NETWORK']['NAME']
        self.vnet_address_prefixes = CONFIG['SUBSCRIPTIONS'][self.name]['VIRTUAL_NETWORK']['ADDRESS_PREFIXES']
        self.subnets = CONFIG['SUBSCRIPTIONS'][self.name]['VIRTUAL_NETWORK']['SUBNETS']

    def get_subnet_address_range(self, subnet_name):
        for subnet_config in self.subnets:
            if subnet_config['NAME'] != subnet_name:
                continue
            else:
                return subnet_config['ADDRESS_PREFIX']
        
        raise ValueError(f"Subnet with name {subnet_name} not found in configuration file")




