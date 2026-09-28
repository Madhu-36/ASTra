from pydantic import BaseModel
class OracleEngineConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
