from pydantic import (
    BaseModel,
    StrictInt,
    StrictStr,
)


class AthenaCalculationStatistics(BaseModel):
    DpuExecutionInMillis: StrictInt
    Progress: StrictStr