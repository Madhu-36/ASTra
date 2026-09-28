from pydantic import BaseModel
class ValkyrieRecoveryConfig(BaseModel):
    auto_recover: bool = True
    jit_enabled: bool = True
