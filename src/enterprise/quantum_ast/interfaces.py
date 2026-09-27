from abc import ABC, abstractmethod
class IQuantumAst(ABC):
    @abstractmethod
    def execute(self):
        pass
