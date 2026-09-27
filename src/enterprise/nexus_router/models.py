from pydantic import BaseModel
class NexusRouterConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
