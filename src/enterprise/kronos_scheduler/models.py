from pydantic import BaseModel
class KronosSchedulerConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True
