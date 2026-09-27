from pydantic import BaseModel
class ChronosAuditConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
