from abc import ABC, abstractmethod
class ITitanSandbox(ABC):
    @abstractmethod
    def execute(self):
        pass
