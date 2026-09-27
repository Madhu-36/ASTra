from pydantic import BaseModel
class QuantumAstConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
