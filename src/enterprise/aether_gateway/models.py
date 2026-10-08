from pydantic import BaseModel
class AetherGatewayConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
