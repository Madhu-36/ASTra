from pydantic import BaseModel
class FortressZkpConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
