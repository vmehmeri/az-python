from Endpoint import Endpoint

class ApplicationSecurityGroup(Endpoint):

    type = "ApplicationSecurityGroup"

    def __init__(self, network_environment, resource_group_name, name):
        self.resource_group_name = resource_group_name
        self.network_environment = network_environment
        self.name = name
        self.id = f"[resourceId(subscriptionId(),'{self.resource_group_name}','Microsoft.Network/ApplicationSecurityGroups/','{self.name}')]"

    def get_type(self):
        return self.type

    def get_json_key(self):
        return "ApplicationSecurityGroups"

    def get_json_value(self):
        return [dict(
            id = self.id
        )]
