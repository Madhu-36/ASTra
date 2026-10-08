from abc import ABC, abstractmethod
class IAetherGateway(ABC):
    @abstractmethod
    def execute(self):
        pass
