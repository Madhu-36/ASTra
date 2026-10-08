from abc import ABC, abstractmethod
class ISolarisEngine(ABC):
    @abstractmethod
    def execute(self):
        pass
