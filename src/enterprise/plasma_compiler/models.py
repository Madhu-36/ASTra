from pydantic import BaseModel
class PlasmaCompilerConfig(BaseModel):
    auto_recover: bool = True
    jit_enabled: bool = True
