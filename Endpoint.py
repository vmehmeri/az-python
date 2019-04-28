from abc import ABC, abstractmethod

class Endpoint(ABC):
    type = None

    def __init__(self, environment):
        self.network_environment = environment
        super().__init__()

    @abstractmethod
    def get_type(self):
        return self.type

    @abstractmethod
    def get_json_key(self):
        pass

    @abstractmethod
    def get_json_value(self):
        pass