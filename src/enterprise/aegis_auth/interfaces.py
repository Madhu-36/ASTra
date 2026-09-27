from abc import ABC, abstractmethod
class IAegisAuth(ABC):
    @abstractmethod
    def execute(self):
        pass
