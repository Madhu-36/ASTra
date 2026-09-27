from abc import ABC, abstractmethod
class IVanguardNetwork(ABC):
    @abstractmethod
    def execute(self):
        pass
