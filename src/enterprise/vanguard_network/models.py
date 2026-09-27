from pydantic import BaseModel
class VanguardNetworkConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
