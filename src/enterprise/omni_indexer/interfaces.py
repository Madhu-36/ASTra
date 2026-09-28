from abc import ABC, abstractmethod
class IOmniIndexer(ABC):
    @abstractmethod
    def execute(self):
        pass
