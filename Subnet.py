from Endpoint import Endpoint
from NetworkEnvironment import NetworkEnvironment

class Subnet(Endpoint):
    type = "Subnet"

    def __init__(self, network_environment, name):
        self.name = name
        self.network_environment = network_environment
        try:
            self.ip_range = self.network_environment.get_subnet_address_range(self.name)
        except ValueError as err:
            print(err)
            self.ip_range = None

    def get_type(self):
        return self.type

    def get_json_key(self):
        return "AddressPrefixes"

    def get_json_value(self):
        return [self.ip_range]