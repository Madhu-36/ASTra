from pydantic import BaseModel
class OpticsTelemetryConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
