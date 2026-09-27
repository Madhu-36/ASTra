from pydantic import BaseModel
class MatrixRatelimitConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
