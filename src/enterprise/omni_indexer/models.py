from pydantic import BaseModel
class OmniIndexerConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
