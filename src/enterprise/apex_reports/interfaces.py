from abc import ABC, abstractmethod
class IApexReports(ABC):
    @abstractmethod
    def execute(self):
        pass
