from abc import ABC, abstractmethod
class IKronosScheduler(ABC):
    @abstractmethod
    def execute(self):
        pass
