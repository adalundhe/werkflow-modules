from pydantic import (
    BaseModel,
    StrictInt,
)


class AthenaSessionStatistics(BaseModel):
    DpuExecutionInMillis: StrictInt