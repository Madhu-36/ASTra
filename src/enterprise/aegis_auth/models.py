from pydantic import BaseModel
class AegisAuthConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
