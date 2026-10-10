from abc import ABC, abstractmethod
class INebulaStorage(ABC):
    @abstractmethod
    def execute(self):
        pass
