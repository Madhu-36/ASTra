from pydantic import BaseModel
class SolarisEngineConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
