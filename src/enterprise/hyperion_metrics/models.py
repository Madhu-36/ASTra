from pydantic import BaseModel
class HyperionMetricsConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
