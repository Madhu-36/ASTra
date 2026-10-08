from abc import ABC, abstractmethod
class IHyperionMetrics(ABC):
    @abstractmethod
    def execute(self):
        pass
