from pydantic import BaseModel
class ApexReportsConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
