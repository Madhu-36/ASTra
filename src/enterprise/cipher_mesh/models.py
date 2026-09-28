from pydantic import BaseModel
class CipherMeshConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
