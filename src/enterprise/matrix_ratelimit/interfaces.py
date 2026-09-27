from abc import ABC, abstractmethod
class IMatrixRatelimit(ABC):
    @abstractmethod
    def execute(self):
        pass
