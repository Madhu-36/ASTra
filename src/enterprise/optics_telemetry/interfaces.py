from abc import ABC, abstractmethod
class IOpticsTelemetry(ABC):
    @abstractmethod
    def execute(self):
        pass
