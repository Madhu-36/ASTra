from pydantic import BaseModel
class SentinelAiConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
