from abc import ABC, abstractmethod
class IChronosAudit(ABC):
    @abstractmethod
    def execute(self):
        pass
