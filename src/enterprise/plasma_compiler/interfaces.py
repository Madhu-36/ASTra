from abc import ABC, abstractmethod
class IPlasmaCompiler(ABC):
    @abstractmethod
    def execute(self):
        pass
