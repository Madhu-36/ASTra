from abc import ABC, abstractmethod
class IPulsarQueue(ABC):
    @abstractmethod
    def execute(self):
        pass
