from abc import ABC, abstractmethod
class ICipherMesh(ABC):
    @abstractmethod
    def execute(self):
        pass
