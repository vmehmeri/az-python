from abc import ABC, abstractmethod
from Endpoint import Endpoint
from ipaddress import ip_network, ip_address

class IpAddress(Endpoint):
    type = "IpAddress"

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    def get_type(self):
        return "IpAddress"

    def get_json_key(self):
        return "AddressPrefixes"

    def get_json_value(self):
        if type(self.ip_addr) is list:
            return self.ip_addr

        return [self.ip_addr]

    def is_in_range(self, cidr_range):
        net = ip_network(cidr_range)
        ip = ip_address(self.ip_addr)

        return ip in net

class AzureIpAddress(IpAddress):
    type = "IpAddress"

    def __init__(self, network_environment, ip_addr):
        self.network_environment = network_environment
        super().__init__(ip_addr)

    def get_parent_subnet(self):
        return ""

class OnPremisesIpAddress(IpAddress):

    def __init__(self, ip_addr):
        self.network_environment = None
        super().__init__(ip_addr)
