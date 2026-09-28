from pydantic import BaseModel
class TitanSandboxConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
