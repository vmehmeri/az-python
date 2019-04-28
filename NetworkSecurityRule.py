from Endpoint import Endpoint
from Subnet import Subnet
from IpAddress import IpAddress

import json

class NetworkSecurityRule:
    def __init__(self, name: str, description: str, priority: int, 
                source: Endpoint, destination: Endpoint, protocol: str, port: int, direction: str, action = "allow"):
        
        self.action = action
        self.name = name
        self.description = description
        self.priority = priority
        self.source = source
        self.destination = destination
        self.protocol = protocol
        self.port = port
        self.direction = direction


    def to_json_object(self):
        dictObject = {}

        dictObject['name'] = self.name
        dictObject['description'] = self.description
        dictObject['priority'] = self.priority
        dictObject['port'] = self.port
        dictObject['protocol'] = self.port
        dictObject['direction'] = self.direction
        dictObject['action'] = self.action

        srcKey = f"source{self.source.get_json_key()}"
        dstKey = f"destination{self.destination.get_json_key()}"

        dictObject[srcKey] = self.source.get_json_value()
        dictObject[dstKey] = self.destination.get_json_value()

        return json.dumps(dictObject, indent=4, sort_keys=True)

    
