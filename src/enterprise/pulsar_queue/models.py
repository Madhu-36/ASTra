from pydantic import BaseModel
class PulsarQueueConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
