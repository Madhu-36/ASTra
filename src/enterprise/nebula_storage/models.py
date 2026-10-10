from pydantic import BaseModel
class NebulaStorageConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
